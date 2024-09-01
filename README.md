# Blockchain API

Esta é uma API de blockchain desenvolvida com FastAPI.

## Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/Benjamim-EP/blockchain-api.git
cd blockchain-api
```
2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```