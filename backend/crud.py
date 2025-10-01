from sqlalchemy.orm import Session
# Importações absolutas corrigidas
import models, schemas 
from datetime import datetime
from sqlalchemy.orm import selectinload

# --- 1. OPERAÇÕES DE CATEGORIA ---

# Função para criar uma nova Categoria no banco de dados
def create_category(db: Session, category: schemas.CategoryCreate):
    # 1. Cria a instância do modelo SQLAlchemy (AQUI ESTÁ A CORREÇÃO!)
    db_category = models.Category( 
        name=category.name,
        type=category.type
    )
    
    # 2. Adiciona, confirma e atualiza
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    
    # 3. Retorna o objeto criado
    return db_category

# Função para listar todas as categorias
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


# --- 2. OPERAÇÕES DE TRANSAÇÃO ---

# Função para criar uma nova Transação
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    # Usa a data atual se não for fornecida
    transaction_date = transaction.date if transaction.date else datetime.utcnow()
    
    # 1. Cria a instância do modelo SQLAlchemy
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        category_id=transaction.category_id,
        date=transaction_date
    )
    
    # 2. Adiciona, confirma e atualiza
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction

# Função para listar todas as transações, carregando os detalhes da Categoria
def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction)\
             .options(selectinload(models.Transaction.category))\
             .offset(skip)\
             .limit(limit)\
             .all()