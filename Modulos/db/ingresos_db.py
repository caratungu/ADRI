from typing import Dict
from pydantic import BaseModel

class AhorroInDB(BaseModel):
    username: str
    date: str
    monto: float
    concepto: str