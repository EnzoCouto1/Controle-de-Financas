from sqlalchemy.orm import Session, selectinload
# Importações absolutas
import models, schemas 
from datetime import datetime

# NOTA: TODAS as importações de 'security' foram removidas do topo.

# --- 1. OPERAÇÕES DE CATEGORIA ---

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category( 
        name=category.name,
        type=category.type
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

# --- 2. OPERAÇÕES DE TRANSAÇÃO ---

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    transaction_date = transaction.date if transaction.date else datetime.utcnow()
    
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        category_id=transaction.category_id,
        date=transaction_date
    )
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction)\
             .options(selectinload(models.Transaction.category))\
             .offset(skip)\
             .limit(limit)\
             .all()

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return db_transaction
    
    return None


# --- 3. OPERAÇÕES DE USUÁRIO (Onde a Correção de Ciclo é CRUCIAL) ---

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):

    # CORREÇÃO ESTRUTURAL: Quebra o ciclo importando DENTRO da função
    from security import get_password_hash 
    
    # Truncagem é feita APÓS a importação, antes do hash
    senha_truncada = user.password[:72] 
    hashed_password = get_password_hash(senha_truncada)

    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def update_transaction(db: Session, transaction_id: int, transaction_data: schemas.TransactionUpdate):
    # 1. Encontra a transação no banco
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if not db_transaction:
        return None # Retorna None se não encontrar

    # 2. Converte os dados Pydantic para um dict, 
    #    excluindo campos que não foram enviados (exclude_unset=True)
    update_data = transaction_data.dict(exclude_unset=True)

    # 3. Atualiza os campos no objeto do SQLAlchemy
    for key, value in update_data.items():
        setattr(db_transaction, key, value)

    # 4. Salva as mudanças
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction