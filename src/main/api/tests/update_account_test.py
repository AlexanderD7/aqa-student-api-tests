import pytest
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel
from src.main.api.models.update_account_request_model import UpdateAccountRequestModel

@allure.epic("Управление студентами")
@allure.feature("PUT операции")
class TestUpdateAccount:

    @pytest.mark.xfail(reason="BUG-3: Студент не сохраняется, поэтому PUT падает")
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

        with allure.step(f"Отправка PUT запроса для студента с ID: {student_id}"):
            update_response = api_manager.account_steps.update_account(student_id, update_request)

        assert update_response.message == "Student updated successfully", (
            f"API вернуло ошибку при обновлении студента {student_id}. "
            f"Ответ API: {update_response.message}"
        )
        assert update_response.student.name == "Updated Name", f"Имя не обновилось для ID {student_id}!"