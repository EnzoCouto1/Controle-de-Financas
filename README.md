# 💰 Sistema de Controle de Finanças Pessoais

![Status](https://img.shields.io/badge/Status-Concluído-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

Uma aplicação web completa (**Full Stack**) para gestão financeira pessoal. O sistema permite que usuários se cadastrem, registrem suas receitas e despesas, categorizem lançamentos e visualizem um dashboard interativo com resumo financeiro e gráficos.

O projeto foi desenvolvido com foco em arquitetura de microsserviços, utilizando **Docker** para orquestração de containers.

## 📸 Screenshots

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma stack moderna e robusta:

### **Backend (API)**
* 🐍 **Python 3.11**
* ⚡ **FastAPI** - Framework de alta performance para construção de APIs.
* 🗄️ **SQLAlchemy** - ORM para interação com o banco de dados.
* 🔒 **Passlib & Bcrypt** - Para hashing seguro de senhas.
* 🔑 **Python-JOSE** - Para geração e validação de tokens JWT.
* ✅ **Pydantic** - Para validação e serialização de dados.

### **Frontend (Interface)**
* ⚛️ **React.js** - Biblioteca para construção de interfaces.
* ⚡ **Vite** - Build tool rápida e leve.
* 📡 **Axios** - Cliente HTTP para comunicação com a API.
* 📊 **Chart.js & React-chartjs-2** - Para visualização de dados (Gráficos).
* 🎨 **CSS3** - Estilização personalizada e responsiva.

### **Infraestrutura & Banco de Dados**
* 🐳 **Docker** & **Docker Compose** - Para containerização e orquestração.
* 🐘 **PostgreSQL** - Banco de dados relacional robusto.

---

## ✨ Funcionalidades

* **Autenticação e Segurança:**
    * Cadastro de novos usuários.
    * Login seguro com geração de Token JWT.
    * Proteção de rotas (apenas usuários logados acessam seus dados).
* **Gestão de Categorias:**
    * Criação de categorias personalizadas (ex: Lazer, Salário).
    * Classificação por Tipo (Receita ou Despesa).
* **Gestão de Transações:**
    * Adicionar novas receitas e despesas.
    * Visualizar histórico de lançamentos.
    * Editar e Excluir transações existentes.
* **Dashboard Interativo:**
    * Resumo financeiro automático (Total Receitas - Total Despesas = Saldo).
    * Gráfico de Pizza para visualização de despesas por categoria.

---

## 🚀 Como Executar o Projeto

Graças ao Docker, você não precisa instalar Python, Node.js ou PostgreSQL na sua máquina. Basta ter o **Docker** e o **Git**.

### Pré-requisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado e rodando.
* [Git](https://git-scm.com/) instalado.

### Passo a Passo

1. **Clone o repositório:**
    ```bash
    # Substitua SEU-USUARIO pelo seu nome de usuário do GitHub
    git clone https://github.com/EnzoCouto1/Controle-de-Financas
    cd Controle-de-Financas
    ```

2. **Configure as variáveis de ambiente (Backend):**
    * Entre na pasta `backend`.
    * Certifique-se de que existe um arquivo `.env` (ou copie o `.env.example` para `.env`).
    * *Nota: O Docker Compose já está configurado para injetar as credenciais padrões.*

3. **Suba a aplicação com Docker Compose:**
    Este comando irá construir as imagens e iniciar o Backend, Frontend e Banco de Dados.
    ```bash
    docker-compose up -d --build
    ```

4. **Acesse a aplicação:**
    * **Frontend (Aplicação Web):** Abra seu navegador em [http://localhost:3000](http://localhost:3000).
    * **Backend (Documentação Swagger):** Acesse [http://localhost:8000/docs](http://localhost:8000/docs).

---

## 📂 Estrutura do Projeto

```text
Controle-de-Financas/
├── backend/                # Código fonte da API (FastAPI)
│   ├── routers/            # Rotas da API (Auth, Users, Transactions, Categories)
│   ├── crud.py             # Lógica de banco de dados
│   ├── database.py         # Configuração do PostgreSQL
│   ├── models.py           # Modelos das tabelas (SQLAlchemy)
│   ├── schemas.py          # Schemas de validação (Pydantic)
│   ├── security.py         # Lógica de Hashing e JWT
│   └── main.py             # Entrada da aplicação
├── frontend/               # Código fonte da Interface (React)
│   ├── src/
│   │   ├── components/     # Componentes (Home, Login, Forms, Charts)
│   │   ├── api.js          # Configuração do Axios e Interceptors
│   │   └── App.jsx         # Componente principal e rotas
├── docker-compose.yml      # Orquestração dos containers
└── README.md               # Documentação do projeto
