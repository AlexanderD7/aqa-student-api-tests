from typing import List
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse

class GetStudentsResponseModel(BaseModel):
    status: int
    students: List[CreateAccountResponse]