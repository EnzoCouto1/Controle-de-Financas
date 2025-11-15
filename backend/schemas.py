from pydantic import BaseModel, EmailStr
from datetime import datetime

# --- 1. SCHEMAS DE CATEGORIA ---

# Schema Base (o que o usuário deve ENVIAR para criar ou atualizar)
class CategoryBase(BaseModel):
    name: str
    type: str  # Ex: "Receita" ou "Despesa"

# Schema de Criação (herda o base)
class CategoryCreate(CategoryBase):
    pass # Não precisa de campos adicionais por enquanto

# Schema de Resposta (o que a API deve RETORNAR)
# O campo 'id' e 'transactions' são adicionados porque eles vêm do banco de dados
class Category(CategoryBase):
    id: int
    # O 'orm_mode = True' permite que o Pydantic leia dados de objetos SQLAlchemy
    class Config:
        from_attributes = True


# --- 2. SCHEMAS DE TRANSAÇÃO ---

# Schema Base (o que o usuário deve ENVIAR)
class TransactionBase(BaseModel):
    description: str
    amount: float
    category_id: int # Chave estrangeira para a categoria
    date: datetime | None = None # Opcional na criação, será setado no backend

# Schema de Criação (herda o base)
class TransactionCreate(TransactionBase):
    # Aqui, você pode definir regras específicas para a criação se necessário
    pass

# Schema de Resposta (o que a API deve RETORNAR)
class Transaction(TransactionBase):
    id: int
    
    # Define a relação que o modelo Transaction tem com o modelo Category
    # Isso garante que, ao retornar uma transação, você possa incluir os detalhes da categoria
    category: Category 
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):  
    email: EmailStr         

class UserCreate(UserBase):
    password: str

class User(UserBase):  
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True

class Token(BaseModel): 
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: str | None = None

class TransactionUpdate(BaseModel):
    description: str | None = None
    amount: float | None = None
    category_id: int | None = None
    
    class Config:
        from_attributes = True