from enum import Enum
from typing import Optional, Type
from dataclasses import dataclass
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_request import CreateAccountRequestModel
from src.main.api.models.create_account_response import CreateAccountResponseModel
from src.main.api.models.delete_account_response_model import DeleteAccountResponseModel


@dataclass
class EndpointConfiguration:
    url:str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class EndpointRequest(Enum):
    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = CreateAccountRequestModel,
        url = '/student' ,
        response_model = CreateAccountResponseModel
    )
    DELETE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "/student/{student_id}",
        response_model = DeleteAccountResponseModel
    )