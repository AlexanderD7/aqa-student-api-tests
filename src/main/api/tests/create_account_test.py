import pytest
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel

@allure.epic("Управление студентами")
@allure.feature("POST операции")
class TestCreateAccount:
    @allure.title("Успешное создание студента с валидными данными")
    @pytest.mark.parametrize("create_account_request", [{}] * 8, indirect=True)
    def test_account_creation_valid(self,api_manager: ApiManager,create_account_request: CreateAccountRequestModel):

        response_model = api_manager.account_steps.create_account(create_account_request)

        assert response_model.message == "Student created successfully"
        assert response_model.student.id > 0
        assert response_model.student.email == create_account_request.email
        assert response_model.student.phone_no == create_account_request.phone_no

    @pytest.mark.xfail(reason="BUG-4: API возвращает 200 OK вместо 400 Bad Request при ошибке валидации status/gender")
    @allure.title("Создание студента с невалидными данными (негативный тест)")
    @pytest.mark.parametrize("invalid_field, invalid_value", [
        ("status", 99),
        ("gender", "unknown"),
    ])
    def test_account_creation_invalid(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel,
                                      invalid_field, invalid_value):
        setattr(create_account_request, invalid_field, invalid_value)

        with allure.step(f"Отправка POST с невалидным полем {invalid_field}: {invalid_value}"):
            api_manager.account_steps.create_invalid_account(create_account_request)