from typing import Optional
from pydantic import BaseModel

class BlockSchema(BaseModel):
    index: int
    data: str
    previous_hash: str
    hash: Optional[str] = None
    nonce: int
