from typing import Optional
from requests import Response
import requests

from src.main.api.configs.config import Config
from src.main.api.foundation.requesters.http_requester import HttpRequester
from src.main.api.models.base_model import BaseModel
import allure

class CrudRequester(HttpRequester):
    def post(self, model: Optional[BaseModel]) -> BaseModel| Response:
        body = model.model_dump() if model is not None else ""
        url = f"{Config.fetch('backendUrl')}{self.endpoint.value.url}"

        with allure.step(f"POST {url}"):
            allure.attach(str(body), "Request body", allure.attachment_type.JSON )

        response = requests.post(
            url = url,
            headers = self.request_spec,
            json = body
        )
        allure.attach(
            response.text,
            "Response body",
            allure.attachment_type.JSON)
        self.response_spec(response)
        return response

    def delete(self, student_id: int) -> Response:
        url = f"{Config.fetch('backendUrl')}{self.endpoint.value.url.format(student_id=student_id)}"

        with allure.step(f"DELETE {url}"):
            pass

        response = requests.delete(
            url=url,
            headers=self.request_spec
        )
        allure.attach(
            response.text,
            "Response body",
            allure.attachment_type.JSON
        )
        self.response_spec(response)
        return response