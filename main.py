from fastapi import FastAPI

app = FastAPI(title="Hybrid Athlete App")

@app.get("/")
def read_root():
    return {"status": "API rodando!"}