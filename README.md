# 🌦️ End-to-End Weather Data Pipeline
 
Este projeto implementa um pipeline completo de dados meteorológicos, desde a extração de uma API externa até a orquestração e armazenamento em um banco de dados relacional.
 
O projeto foi desenvolvido com foco em:
- ETL (nível iniciante)
- Orquestração com Airflow e Docker (nível intermediário)
## 🏗️ Arquitetura e Tecnologias
 
O pipeline segue o modelo ETL (Extract, Transform, Load):
 
| Componente | Tecnologia |
|-----------|-----------|
| **Fonte de Dados** | API OpenWeatherMap |
| **Processamento** | Python + Pandas |
| **Destino** | PostgreSQL |
| **Orquestração** | Apache Airflow (TaskFlow API) |
| **Infraestrutura** | Docker + Docker Compose |
| **Gerenciamento de Pacotes** | UV |
 
## 📂 Estrutura do Projeto
 
```
.
├── dags/              # Definições das DAGs do Airflow
├── src/               # Scripts modulares de ETL
├── data/              # Dados temporários (.json, .parquet)
├── config/            # Variáveis de ambiente e configs
├── notebooks/         # Análises exploratórias (Jupyter)
└── README.md          # Este arquivo
```
 
## 🚀 Como Executar o Projeto
 
### 1. Pré-requisitos
 
- Docker Desktop instalado
- Python 3.12+
- API Key do OpenWeatherMap (Opcional)
- WSL2 no Windows
### 2. Configuração do Banco de Dados
 
Execute os comandos abaixo no PostgreSQL:
 
```sql
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
ALTER USER seu_usuario WITH SUPERUSER;
CREATE DATABASE weather_data OWNER seu_usuario;
```
 
### 3. Variáveis de Ambiente
 
Crie um arquivo `.env` dentro da pasta `config/`:
 
```env
user=seu_usuario
password=sua_senha
database=weather_data
api_key=sua_chave_da_api
```
 
⚠️ **Nota**: O projeto utiliza `quote_plus` para tratar caracteres especiais na senha.
 
### 4. Inicialização com Docker
 
Na raiz do projeto:
 
#### (Opcional) Ambiente virtual com UV
 
```bash
uv init
uv venv
```
 
#### Subir os serviços
 
```bash
docker compose up -d
```
 
Acesse o Airflow em: **http://localhost:8080**
 
Usuário/Senha padrão: `airflow`
 
## ⚙️ Pipeline (DAG)
 
A DAG `YouTube_Weather_Pipeline` é executada a cada 1 hora.
 
### 🔹 Etapas:
 
#### **Extract**
Coleta dados meteorológicos de São Paulo via API e salva em JSON
 
#### **Transform**
- Normaliza colunas complexas
- Converte tipos de dados (ex: timestamp → datetime no fuso de SP)
- Remove colunas desnecessárias
#### **Load**
Insere os dados no PostgreSQL utilizando SQLAlchemy
 
## 📊 Objetivo do Projeto
 
Demonstrar na prática:
- ✅ Construção de pipelines de dados
- ✅ Orquestração com Airflow
- ✅ Containerização com Docker
- ✅ Boas práticas de organização de projetos de dados
## 📚 Referência
 
Projeto baseado no tutorial de **vbluuiza**
 
