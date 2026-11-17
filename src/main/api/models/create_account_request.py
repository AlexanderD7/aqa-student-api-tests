from src.main.api.models.base_model import BaseModel
from typing import Literal
from typing import Annotated
from pydantic import BeforeValidator
from pydantic import Field
from src.main.api.generators.generator_number import CreationRule, generate_by_regex

email_rule = CreationRule(regex=r"^[a-z]{5,8}@example\.com$")
phone_rule = CreationRule(regex=r"^\+7\d{10}$")

def generate_phone_if_missing(value: str | None) -> str:
    if value is None:
        return generate_by_regex(phone_rule)
    return value

class CreateAccountRequestModel(BaseModel):
    email: Annotated[str, CreationRule(regex=r"^[a-z]{5,8}@example\.com$")]
    gender: Literal["male", "female"]
    name: str
    # Добавляем CreationRule сюда:
    phone_no: Annotated[str, CreationRule(regex=r"^\+7\d{10}$"), BeforeValidator(generate_phone_if_missing)] = Field(
        default=None, validate_default=True
    )
    status: Literal[0, 1]
