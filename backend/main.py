from fastapi import FastAPI
import models 
from database import engine 
from routers import categories
from routers import transactions


# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)
# --------------------------------------------------

app = FastAPI(
    title="Controle de Finanças Pessoais - API",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(transactions.router)

@app.get("/")
def read_root():
    return {"status": "online", "message": "API de Finanças funcionando!"}
