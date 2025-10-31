from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    DateTime, 
    ForeignKey, 
    Boolean
)
from sqlalchemy.orm import relationship
from database import Base # Corrigido: importação absoluta
from datetime import datetime

# --- 1. MODELO DE CATEGORIA ---
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)  # Ex: "Receita" ou "Despesa"

    # Define a relação inversa: permite acessar as transações de uma categoria
    transactions = relationship("Transaction", back_populates="category")


# --- 2. MODELO DE TRANSAÇÃO ---
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    
    # Foreign Key para a tabela de categorias
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    # Campo de data/hora (configurado para a hora atual por padrão)
    date = Column(DateTime, default=datetime.utcnow)
    
    # Coluna para a relação: permite acessar a categoria de uma transação
    category = relationship("Category", back_populates="transactions")
    
    # Futuramente, adicionaremos user_id (ForeignKey para a tabela de usuários)

class User(Base): # <--- VERIFIQUE SE ESTÁ EXATAMENTE ASSIM
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    # Coluna para armazenar a senha HASHED
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)