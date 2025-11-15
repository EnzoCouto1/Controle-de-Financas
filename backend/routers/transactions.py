# backend/routers/transactions.py

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from security import get_current_user

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
def create_new_transaction(
    transaction: schemas.TransactionCreate, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user) 
):
    print(f"Usuário Autenticado: {current_user.email}")
    return crud.create_transaction(db=db, transaction=transaction)

# Rota GET: Lista todas as transações
@router.get("/", response_model=List[schemas.Transaction])
def list_transactions(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user) # <-- ROTA PROTEGIDA
):
    # Por enquanto, apenas listamos todas as categorias.
    # Em um projeto real, você filtraria por user_id.
    print(f"Usuário Autenticado: {current_user.email}")
    return crud.get_transactions(db=db)

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction_by_id(
    transaction_id: int, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user) 
):
    deleted_transaction = crud.delete_transaction(db, transaction_id=transaction_id)
    
    if deleted_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transação com ID {transaction_id} não encontrada."
        )
        
    # Retorno limpo e explícito:
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch("/{transaction_id}", response_model=schemas.Transaction)
def update_transaction_by_id(
    transaction_id: int,
    transaction_data: schemas.TransactionUpdate, # 1. Usa o novo schema
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user) # 2. Protegido
):
    # 3. Chama a função do CRUD
    updated_transaction = crud.update_transaction(
        db, 
        transaction_id=transaction_id, 
        transaction_data=transaction_data
    )
    
    # 4. Trata se não encontrar
    if updated_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transação com ID {transaction_id} não encontrada."
        )
        
    return updated_transaction