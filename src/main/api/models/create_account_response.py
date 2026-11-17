from src.main.api.models.base_model import BaseModel
from typing import Literal

class CreateAccountResponse(BaseModel):
    email: str
    gender: Literal["male", "female"]
    id: int
    name: str
    phone_no: str
    status: int
class CreateAccountResponseModel(BaseModel):
    message: str
    status: int
    student: CreateAccountResponse
