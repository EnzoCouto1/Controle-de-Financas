# Usa uma imagem base oficial do Node para construir (instalar dependências)
FROM node:20-alpine AS build

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de configuração de dependências
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código
COPY . .

# Comando para rodar a aplicação em modo de desenvolvimento
# O --host 0.0.0.0 é crucial para que o container seja acessível externamente
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]