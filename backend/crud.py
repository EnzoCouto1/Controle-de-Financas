from sqlalchemy.orm import Session, selectinload
# Importações absolutas corrigidas
import models, schemas 
from datetime import datetime
from security import get_password_hash # Importa a função de hashing

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


def delete_transaction(db: Session, transaction_id: int):
    # 1. Encontra a transação pelo ID
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    # 2. Se a transação existir, exclui e confirma
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        # Retorna o objeto excluído, embora na prática o cliente receba 204 No Content
        return db_transaction
    
    # 3. Retorna None se a transação não for encontrada
    return None


# Função para buscar um usuário pelo email (necessário para login e cadastro)
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first() # <--- ESSA É A FUNÇÃO QUE FALTAVA!

# Função para criar um novo Usuário
def create_user(db: Session, user: schemas.UserCreate):
    # 1. Gera o hash da senha (AGORA COM TRUNCAGEM AQUI)
    # O user.password é a string da senha.
    senha_truncada = user.password[:72] 
    hashed_password = get_password_hash(senha_truncada)

    # 2. Cria a instância do modelo SQLAlchemy
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    
    # 3. Adiciona, confirma e atualiza
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user