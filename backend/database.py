from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env.example (ou .env se você copiar)
load_dotenv(os.path.join(os.path.dirname(__file__), ".env.example"))

# Constrói a URL de conexão
# Lembre-se: 'db' é o nome do serviço no docker-compose!
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Cria o motor (engine) de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma sessão, que será usada para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos os modelos do SQLAlchemy
Base = declarative_base()

# Função de utilidade para obter a sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()