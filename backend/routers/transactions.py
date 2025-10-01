# backend/routers/transactions.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Lembre-se, use importações absolutas aqui
import schemas, crud 
from database import get_db

# Cria um roteador específico para as rotas de Transação
router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# Rota POST: Cria uma nova transação
@router.post("/", response_model=schemas.Transaction, status_code=status.HTTP_201_CREATED)
def create_new_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    # A categoria_id é validada pelo Pydantic, o CRUD fará o resto
    return crud.create_transaction(db=db, transaction=transaction)

# Rota GET: Lista todas as transações
@router.get("/", response_model=List[schemas.Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db=db)