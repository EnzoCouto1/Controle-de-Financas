import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Configure o logger (para vermos mensagens no console)
logger = logging.getLogger(__name__)

# Função para aguardar a conexão
def wait_for_db(engine):
    MAX_RETRIES = 10
    RETRY_DELAY = 3 # segundos

    for i in range(MAX_RETRIES):
        try:
            # Tenta se conectar
            engine.connect()
            logger.info("Database connection established!")
            return
        except OperationalError:
            logger.warning(f"Database not ready. Waiting... ({i+1}/{MAX_RETRIES})")
            time.sleep(RETRY_DELAY)
    
    # Se todas as tentativas falharem
    raise Exception("Failed to connect to the database after multiple retries.")