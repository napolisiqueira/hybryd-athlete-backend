import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import init_db
import pandas as pd
import numpy as np

# Importações essenciais do seu projeto
from app.models.alimentos import Alimentos  

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()

        print("Limpando registros antigos defeituosos do MongoDB...")
        await Alimentos.delete_all()

        # 1. Lê o CSV puramente como texto para o Pandas não tentar adivinhar nada errado
        df = pd.read_csv("./alimentos.csv", sep=";", dtype=str)
        df.columns = df.columns.str.strip()

        mapeamento_colunas = {
            "Descrição dos alimentos": "nome",
            "Energia (kcal)": "calorias",
            "Proteína (g)": "proteina",
            "Carboidrato (g)": "carboidrato",
            "Lipídeos (g)": "gordura" 
        }

        df.rename(columns=mapeamento_colunas, inplace=True)
        colunas_finais = list(mapeamento_colunas.values())
        dados_filtrados = df[colunas_finais].copy()

        # 2. TRATAMENTO INFALÍVEL TEXTO -> NÚMERO
        for col in ["calorias", "proteina", "carboidrato", "gordura"]:
            # Transforma em string limpa e remove todos os espaços ao redor
            dados_filtrados[col] = dados_filtrados[col].astype(str).str.strip()
            
            # Substitui a vírgula brasileira por ponto americano (crucial antes do to_numeric)
            dados_filtrados[col] = dados_filtrados[col].str.replace(",", ".", regex=False)
            
            # Limpa qualquer espaço em branco interno residual
            dados_filtrados[col] = dados_filtrados[col].str.replace(r'\s+', '', regex=True)
            
            # Substitui os textos conhecidos da TACO por um nulo real do NumPy
            dados_filtrados[col] = dados_filtrados[col].replace(["Tr", "NA", "-", "---", "nan", "None", ""], np.nan)
            
            # Agora o to_numeric vai funcionar perfeitamente porque só existem números com pontos ou nulos
            dados_filtrados[col] = pd.to_numeric(dados_filtrados[col], errors='coerce')

        alimentos = dados_filtrados.to_dict(orient="records")
        print(f"Total de alimentos prontos para o banco: {len(alimentos)}")
        
        # 3. SALVAMENTO NO MONGODB
        for linha in alimentos:
            # Pula linhas inválidas ou o próprio cabeçalho caso esteja duplicado no arquivo
            if pd.isna(linha['nome']) or str(linha['nome']).strip() == "" or linha['nome'] == "Descrição dos alimentos":
                continue
                
            # Garante que os NaNs do NumPy virem None (null legítimo no Mongo)
            linha_limpa = {k: (None if pd.isna(v) else v) for k, v in linha.items()}
            
            alimento_db = Alimentos(**linha_limpa)
            await alimento_db.insert()
            
        print("🎉 Sucesso absoluto! Todos os alimentos e macros foram povoados corretamente.")
                
    except FileNotFoundError:
        print("Arquivo alimentos.csv não encontrado. Pulando importação.")
    except Exception as e:
        print(f"Erro na importação: {e}")
    yield 
    print("Aplicação finalizada.")

app = FastAPI(lifespan=lifespan, title="Hybrid Athlete App")
