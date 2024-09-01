from typing import List, Optional
from app.models.block import Block

class BlockchainService:
    blockchain: List[Block] = []

    @staticmethod
    def get_blocks() -> List[Block]:
        return BlockchainService.blockchain

    @staticmethod
    def create_genesis_block() -> Block:
        """Cria o bloco gênesis e o adiciona à blockchain."""
        genesis_block = Block(
            index=0,
            data="Bloco Gênesis",
            previous_hash="0",
            nonce=0
        )
        genesis_block.hash = genesis_block.calculate_hash()
        BlockchainService.blockchain.append(genesis_block)
        return genesis_block

    @staticmethod
    def add_block(data: str) -> Optional[Block]:
        """Adiciona um novo bloco à blockchain após gerar o hash e validar a prova de trabalho."""
        last_block = BlockchainService.blockchain[-1] if BlockchainService.blockchain else BlockchainService.create_genesis_block()
        
        new_block = Block(
            index=last_block.index + 1,
            data=data,
            previous_hash=last_block.hash,
            nonce=0
        )

        # Prova de Trabalho para minerar o bloco
        BlockchainService.mine_block(new_block)
        
        BlockchainService.blockchain.append(new_block)
        return new_block

    @staticmethod
    def mine_block(block: Block, difficulty: int = 4) -> None:
        """Função de mineração simples com prova de trabalho."""
        assert block.hash is None, "Bloco já foi minerado"
        prefix_str = '0' * difficulty
        while block.hash is None or not block.hash.startswith(prefix_str):
            block.nonce += 1
            block.hash = block.calculate_hash()
