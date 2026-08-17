# 🏋️ Hybrid Athlete API

API para atletas híbridos — uma plataforma que une **treino de força**, **nutrição**, **corrida** e **saúde** em um só lugar, com histórico completo, análise de progressão e, futuramente, recomendações por IA.

> Pensa em Hevy + MyFitnessPal + Nike Run Club, só que tudo integrado e puxando dados uns dos outros (sono e clima afetando treino, por exemplo).

---

## 📋 Sobre o projeto

A maioria dos apps de fitness cobre só um pedaço da rotina de um atleta: ou é treino, ou é dieta, ou é corrida. O **Hybrid Athlete API** existe pra ser o backend de um app único que acompanha o atleta híbrido (musculação + corrida) de ponta a ponta:

- 🏋️ **Treino** — banco de exercícios com grupo muscular e equipamento, montagem de treinos, execução com registro de séries/reps/carga, histórico e progressão (estilo Hevy)
- 🥗 **Dieta** — banco de alimentos baseado na Tabela TACO, montagem de refeições com cálculo automático de macros, dieta base editável, totais diários e hidratação (estilo MyFitnessPal)
- 🏃 **Corrida** — registro de corridas, pace, distância, rota via GPX (estilo Nike Run Club)
- ❤️ **Saúde** — sono, clima e histórico de dores/lesões, cruzando dados com o desempenho nos treinos
- 🤖 **IA** — recomendações personalizadas de treino, dieta e sono com base no histórico do usuário

Este repositório contém **apenas o backend**. O app mobile (Flutter) consome esta API e vive em um repositório separado.

---

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12 |
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Banco de dados | MongoDB (Atlas) |
| ODM | [Beanie](https://beanie-odm.dev/) (sobre Motor, assíncrono) |
| Validação | Pydantic v2 |
| Gerenciador de pacotes/venv | [uv](https://docs.astral.sh/uv/) (Astral) |
| Autenticação | JWT (OAuth2) |
| IA | API da Anthropic (Claude) |

---

## 🚀 Rodando o projeto localmente

### Pré-requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado
- Uma conta no [MongoDB Atlas](https://www.mongodb.com/atlas) (ou MongoDB local via Docker)

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/hybrid-athlete-api.git
cd hybrid-athlete-api

# Instale as dependências (uv cria o .venv automaticamente)
uv sync

# Copie o arquivo de variáveis de ambiente e preencha com sua connection string do Mongo
cp .env.example .env

# Rode a API
uv run uvicorn main:app --reload
```

A API sobe em `http://127.0.0.1:8000`.
Documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

### Variáveis de ambiente

Crie um arquivo `.env` na raiz com:

```env
MONGODB_URL=mongodb+srv://usuario:senha@seu-cluster.mongodb.net
DATABASE_NAME=hybrid_athlete
SECRET_KEY=sua-chave-secreta-para-jwt
```

---

## 📁 Estrutura do projeto

```
hybrid-athlete-api/
├── app/
│   ├── models/        # Schemas do MongoDB (Beanie/Pydantic)
│   ├── routers/        # Endpoints da API
│   ├── services/        # Lógica de negócio
│   └── core/            # Configurações, conexão com banco, segurança
├── main.py               # Ponto de entrada da aplicação
├── pyproject.toml        # Dependências (gerenciado via uv)
├── uv.lock                # Lockfile de dependências
└── .env.example
```

---

## 🗺️ Roadmap

- [x] Fase 1 — Setup do projeto, banco de exercícios e alimentos (Tabela TACO)
- [ ] Fase 2 — Treinos: criação, execução, histórico e progressão
- [ ] Fase 3 — Dieta: refeições, macros e hidratação
- [ ] Fase 4 — Corrida: registro, GPX e estatísticas
- [ ] Fase 5 — Saúde: sono, clima, lesões e autenticação (JWT)
- [ ] Fase 6 — IA de recomendação e deploy

---

## 📱 App mobile

O app consome esta API e é construído em **Flutter**. Repositório: *[link do repo do app aqui]*

---

## 📄 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.