from typing import Literal
from src.main.api.models.base_model import BaseModel

class UpdateAccountRequestModel(BaseModel):
    email: str
    gender: Literal["male", "female"]
    name: str
    status: Literal[0, 1]