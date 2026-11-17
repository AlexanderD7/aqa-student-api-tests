from typing import Optional
from src.main.api.models.base_model import BaseModel
from src.main.api.foundation.requesters.http_requester import HttpRequester
from src.main.api.foundation.requesters.crud_requester import CrudRequester

class ValidateCrudRequester(HttpRequester):
    def __init__(self, request_spec,endpoint, response_spec):
        super().__init__(request_spec,endpoint,response_spec)
        self.crud_requester=CrudRequester(
            request_spec = request_spec,
            endpoint = endpoint,
            response_spec = response_spec
        )

    def post(self, model: BaseModel) -> BaseModel:
        response = self.crud_requester.post(model)
        return self.endpoint.value.response_model(**response.json())

    def delete(self, student_id: int) -> BaseModel:
        response = self.crud_requester.delete(student_id = student_id)
        return self.endpoint.value.response_model(**response.json())
    def get(self, student_id: Optional[int] = None) -> BaseModel:
        response = self.crud_requester.get(student_id = student_id)
        return self.endpoint.value.response_model(**response.json())
    def put(self, model: BaseModel, student_id: int) -> BaseModel:
        response = self.crud_requester.put(model, student_id=student_id)
        return self.endpoint.value.response_model(**response.json())