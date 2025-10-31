# Usa uma imagem base oficial do Python (versão que você escolheu)
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da sua aplicação
COPY . .

# Comando para rodar a aplicação usando Uvicorn
CMD ["uvicorn", "main:app", "--app-dir", "/app", "--host", "0.0.0.0", "--port", "8000", "--reload"]