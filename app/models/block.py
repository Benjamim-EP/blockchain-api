import hashlib
from typing import Optional
from pydantic import BaseModel

class Block(BaseModel):
    index: int
    data: str
    previous_hash: str
    hash: Optional[str] = None
    nonce: int

    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()
