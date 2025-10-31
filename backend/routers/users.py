from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importações absolutas
import schemas, crud
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Rota de Cadastro de Novo Usuário
@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Checa se o usuário já existe
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        # Retorna erro 400 Bad Request se o e-mail já estiver em uso
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado."
        )
    
    # 2. Se não existir, cria o novo usuário (com senha hashed)
    return crud.create_user(db=db, user=user)