from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import os

# Importações absolutas
import schemas, crud
from database import get_db

pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto",
    # MUDANÇA: Usa um argumento nomeado limpo para aplicar o fix do Bcrypt
    # Isso é necessário para evitar o erro de inicialização/execução no Docker.
    bcrypt__ident='2b' 
)

# backend/security.py
def get_password_hash(password: str) -> str:
    # Remova o [:72] daqui temporariamente, vamos colocar no CRUD
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# --- Configuração de JWT (Tokens) ---

# Use variáveis de ambiente (SECRET_KEY)
SECRET_KEY = os.getenv("SECRET_KEY", "UMA_CHAVE_SECRETA_LONGA_E_RANDOMICA_PARA_PRODUCAO") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Define o esquema de autenticação (usado para injeção de dependência)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    # Adicione o campo 'sub' (subject) se estiver faltando, pois é obrigatório pelo JWT
    if 'sub' not in to_encode:
        # Se for o login, 'sub' já estará na entrada de dados
        pass 
        
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     
    to_encode.update({"exp": expire}) 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função que extrai o usuário do token (para proteger as rotas)
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub") # 'sub' é onde guardamos o e-mail no token
        
        if email is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(email=email)
        
    except JWTError:
        raise credentials_exception
    
    # Busca o usuário no banco de dados
    user = crud.get_user_by_email(db, email=token_data.email)
    
    if user is None:
        raise credentials_exception
        
    return user