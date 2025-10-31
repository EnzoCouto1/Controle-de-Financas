from fastapi import FastAPI
import models 
from database import engine 
from routers import categories
from routers import transactions
from routers import users 
from routers import auth 
from database_utils import wait_for_db 

# 1. Aguarda o banco de dados ficar disponível (boa prática)
wait_for_db(engine)

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Controle de Finanças Pessoais - API",
    version="1.0.0"
)

# Apenas uma inclusão para cada roteador
app.include_router(categories.router)
app.include_router(transactions.router) # CORRIGIDO: Apenas uma vez
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"status": "online", "message": "API de Finanças funcionando!"}