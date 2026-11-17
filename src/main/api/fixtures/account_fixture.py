import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_account_request import CreateAccountRequestModel


@pytest.fixture
def create_account_request(request) -> CreateAccountRequestModel:
    model = RandomModelGenerator.generate(CreateAccountRequestModel)
    if hasattr(request, "param") and isinstance(request.param, dict):
        for key, value in request.param.items():
            setattr(model, key, value)
    return model