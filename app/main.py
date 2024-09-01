from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import blockchain

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:3000",  # Origem do seu frontend React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir essas origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)


# Inclui o roteador do módulo blockchain
app.include_router(blockchain.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Blockchain"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
