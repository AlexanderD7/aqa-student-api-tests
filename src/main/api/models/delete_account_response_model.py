from src.main.api.models.base_model import BaseModel


class DeleteAccountResponseModel(BaseModel):
    message: str
    status: int
