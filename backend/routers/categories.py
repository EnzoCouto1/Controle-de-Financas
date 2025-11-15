from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from security import get_current_user

import schemas, crud
from database import get_db

# Cria um roteador específico para as rotas de Categoria
router = APIRouter(
    prefix="/categories",
    tags=["Categories"] # Tag para organizar a documentação Swagger
)

# Rota POST: Cria uma nova categoria
@router.post("/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_new_category(
    category: schemas.CategoryCreate, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    # Agora você sabe quem é o usuário (current_user.id)
    print(f"Usuário Autenticado: {current_user.email}")
    return crud.create_category(db=db, category=category)

# Rota GET: Lista todas as categorias
@router.get("/", response_model=List[schemas.Category])
def list_categories(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user) # <-- ROTA PROTEGIDA
):
    # Por enquanto, apenas listamos todas as categorias.
    # Em um projeto real, você filtraria por user_id.
    print(f"Usuário Autenticado: {current_user.email}")
    return crud.get_categories(db=db)