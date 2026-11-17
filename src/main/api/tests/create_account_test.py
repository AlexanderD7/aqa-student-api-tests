import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel


class TestCreateAccount:
    @pytest.mark.parametrize("create_account_request", [{}] * 8, indirect=True)
    def test_account_creation_valid(self,api_manager: ApiManager,create_account_request: CreateAccountRequestModel):

        response_model = api_manager.account_steps.create_account(create_account_request)

        assert response_model.message == "Student created successfully"
        assert response_model.student.id > 0
        assert response_model.student.email == create_account_request.email
        assert response_model.student.phone_no == create_account_request.phone_no