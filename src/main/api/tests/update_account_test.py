import pytest
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel
from src.main.api.models.update_account_request_model import UpdateAccountRequestModel

@allure.epic("Управление студентами")
@allure.feature("PUT операции")
class TestUpdateAccount:

    @pytest.mark.xfail(reason="Ожидаем падение из-за бага с сохранением (BUG-1: Eventual Consistency)")
    @allure.title("Успешное обновление данных студента")
    def test_update_account(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
        create_response = api_manager.account_steps.create_account(create_account_request)
        student_id = create_response.student.id

        update_request = UpdateAccountRequestModel(
            email="updated_email@example.com",
            gender="female",
            name="Updated Name",
            status=0
        )

        with allure.step(f"Обновление данных студента ID: {student_id}"):
            update_response = api_manager.account_steps.update_account(student_id, update_request)

        assert update_response.message == "Student updated successfully"
        assert update_response.student.name == "Updated Name"
        assert update_response.student.email == "updated_email@example.com"