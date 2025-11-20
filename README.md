# 🔑 Serviço de Autenticação - Gerenciador de Estoque

![Status](https://img.shields.io/badge/status-em--desenvolvimento-yellow)

Este repositório contém o código-fonte de um microsserviço de autenticação dedicado para o projeto de **Gerenciamento de Estoque**. Sua única responsabilidade é gerenciar a identidade dos usuários e emitir tokens de acesso (JWT).

## 🛠️ Tecnologias Utilizadas

-   **[Python](https://www.python.org/)**
-   **[Django](https://www.djangoproject.com/)** & **[Django REST Framework](https://www.django-rest-framework.org/)**
-   **[Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)**: Para geração e validação de JSON Web Tokens.
-   **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados dos usuários.
-   **[Docker](https://www.docker.com/)** & **[Docker Compose](https://docs.docker.com/compose/)**: Para containerização do serviço.

## 🔗 Repositórios do Projeto

Este projeto é dividido em múltiplos repositórios. Acesse os outros componentes através dos links abaixo:

-   **[📄 Documentação](https://github.com/EcoStock-organization/ecostock-docs)**
-   **[⚙️ Backend](https://github.com/EcoStock-organization/ecostock-backend)**
-   **[🖥️ Frontend](https://github.com/EcoStock-organization/ecostock-frontend)**

## 🚀 Como Rodar o Projeto

Este serviço é totalmente containerizado. Você só precisa do Docker instalado.

### Pré-requisitos

-   **[Docker](https://docs.docker.com/get-docker/)**
-   **[Docker Compose](https://docs.docker.com/compose/install/)**

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/EcoStock-organization/ecostock-auth.git
    cd Auth
    ```

2.  **Crie o arquivo de variáveis de ambiente:**
    Este serviço usa um arquivo `.env` para as credenciais do banco de dados e a chave secreta do Django.
    ```bash
    cp .env.example .env
    ```
    *(Nota: Certifique-se de que o arquivo `.env` gerado contenha valores válidos, especialmente para `DJANGO_SECRET_KEY`)*.

3.  **Construa e inicie os contêineres:**
    ```bash
    docker-compose up --build -d
    ```

4.  **Execute as migrações do banco de dados:**
    Este comando cria as tabelas de usuário, grupos e permissões.
    ```bash
    docker-compose exec auth_backend python src/manage.py migrate
    ```

5.  **Crie um usuário para testes:**
    ```bash
    docker-compose exec auth_backend python src/manage.py createsuperuser
    ```
    (Siga as instruções no terminal para definir o nome, email e senha).

Pronto! O serviço de autenticação estará rodando em **[http://localhost:8001](http://localhost:8001)**.

## 📌 Endpoints da API

### 1. Obter Token de Acesso

-   **Método:** `POST`
-   **URL:** `http://localhost:8001/api/token/`
-   **Body (JSON):**
    ```json
    {
        "username": "seu-usuario",
        "password": "sua-senha"
    }
    ```
-   **Resposta de Sucesso (200 OK):**
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

### 2. Atualizar Token de Acesso

-   **Método:** `POST`
-   **URL:** `http://localhost:8001/api/token/refresh/`
-   **Body (JSON):**
    ```json
    {
        "refresh": "seu-token-de-refresh-aqui"
    }
    ```
-   **Resposta de Sucesso (200 OK):**
    ```json
    {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```
