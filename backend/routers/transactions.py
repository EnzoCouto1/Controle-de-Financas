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

# ----------------- NOVA ROTA (DELETE) -----------------
@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    # 1. Tenta excluir a transação
    deleted_transaction = crud.delete_transaction(db, transaction_id=transaction_id)
    
    # 2. Se não encontrar, retorna 404
    if deleted_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transação com ID {transaction_id} não encontrada."
        )
        
    # 3. Se encontrar e excluir, o FastAPI retornará 204 No Content (como definido no decorador)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# ------------------------------------------------------