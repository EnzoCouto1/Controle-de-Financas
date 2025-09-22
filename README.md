# Controle de Finanças 💸

![Badge de Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Badge de Licença](https://img.shields.io/badge/license-MIT-blue)

## 📝 Descrição do Projeto

É um sistema web para controle de finanças pessoais, desenvolvido como projeto final acadêmico. A plataforma permite que os usuários cadastrem suas receitas e despesas de forma categorizada, oferecendo uma visão clara e organizada da sua vida financeira.
## ✨ Funcionalidades Principais

-   ✅ **Autenticação de Usuários:** Sistema seguro de cadastro e login.
-   ✅ **CRUD de Lançamentos:** Crie, leia, atualize e delete transações financeiras.
-   ✅ **Categorização:** Associe cada lançamento a uma categoria (Ex: Moradia, Lazer, Salário).
-   ✅ **Dashboard Intuitivo:** Visualize um resumo do balanço mensal e os últimos lançamentos.
-   ✅ **Containerização:** Toda a aplicação roda em containers Docker, garantindo portabilidade e um ambiente de desenvolvimento consistente.

## 🛠️ Tecnologias Utilizadas

Este projeto é dividido em três serviços principais, orquestrados com Docker Compose:

-   **Backend:**
    -   [Python 3.11](https://www.python.org/)
    -   [FastAPI](https://fastapi.tiangolo.com/) - Framework web para a construção da API REST.
    -   [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para comunicação com o banco de dados.

-   **Frontend:**
    -   [React](https://reactjs.org/)
    -   [Axios](https://axios-http.com/) - Para realizar as chamadas à API.

-   **Banco de Dados:**
    -   [PostgreSQL](https://www.postgresql.org/)

-   **Infraestrutura e Deploy:**
    -   [Docker](https://www.docker.com/)
    -   [Docker Compose](https://docs.docker.com/compose/)

## 🚀 Como Executar o Projeto

Para rodar este projeto em seu ambiente local, siga os passos abaixo.

### Pré-requisitos

-   [Git](https://git-scm.com/)
-   [Docker](https://www.docker.com/products/docker-desktop)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/EnzoCouto1/Controle-de-Financas
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd !!SEU-REPOSITORIO!!(Em desenvolvimento)
    ```

3.  **Crie um arquivo de variáveis de ambiente:**
    * No backend, pode haver um arquivo `.env.example`. Copie-o para um novo arquivo `.env` e preencha as variáveis necessárias, como as credenciais do banco de dados.
    ```bash
    # Exemplo - dentro da pasta /backend
    cp .env.example .env
    ```

4.  **Suba os containers com Docker Compose:**
    * Este comando irá construir as imagens e iniciar os containers do backend, frontend e banco de dados em modo detached (-d).
    ```bash
    docker-compose up -d --build
    ```

5.  **Acesse a aplicação:**
    * **Frontend:** Abra seu navegador e acesse `http://localhost:3000`
    * **Backend (Documentação da API):** Acesse `http://localhost:8000/docs`

## 👨‍💻 Autor

Feito por **[Enzo Couto]**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/EnzoCouto1)
