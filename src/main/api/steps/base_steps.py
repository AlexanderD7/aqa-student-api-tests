from typing import List
from typing import Any


class BaseSteps:
    def __init__(self, created_obj: List[Any]):
        self.created_obj = created_obj