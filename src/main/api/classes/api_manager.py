from typing import Any, List

from src.main.api.steps.account_steps import AccountSteps


class ApiManager:
    def __init__(self, created_obj: List[Any]):
        self.account_steps = AccountSteps(created_obj)