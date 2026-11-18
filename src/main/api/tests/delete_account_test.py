import pytest
import requests
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel


@allure.epic("Управление студентами")
@allure.feature("DELETE операции")
class TestDeleteAccount:
    @allure.title("Успешное удаление студента")
    def test_delete_account_validate(self,api_manager: ApiManager,create_account_request: CreateAccountRequestModel):
        response_model = api_manager.account_steps.create_account(create_account_request)
        student_id = response_model.student.id
        with allure.step(f"Отправка DELETE запроса для ID: {student_id}"):
            delete_response = api_manager.account_steps.delete_account(student_id)
        assert delete_response.message == "Student deleted successfully"
        assert delete_response.status == 1
