from fastapi import APIRouter, HTTPException
from app.schemas.block_schema import BlockSchema
from pydantic import BaseModel
from app.services.blockchain_service import BlockchainService
from typing import List

router = APIRouter(
    prefix="/blockchain",
    tags=["blockchain"]
)

class DataSchema(BaseModel):
    data: str

@router.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Blockchain"}

@router.get("/blocks", response_model=List[BlockSchema])
def get_all_blocks():
    """
    Retorna todos os blocos existentes na blockchain.
    """
    blocks = BlockchainService.get_blocks()
    return blocks

@router.post("/", response_model=BlockSchema)
def add_block(block_data: DataSchema):
    """
    Adiciona um novo bloco à blockchain.
    """
    new_block = BlockchainService.add_block(block_data.data)
    if not new_block:
        raise HTTPException(status_code=400, detail="Não foi possível adicionar o bloco.")
    return new_block
