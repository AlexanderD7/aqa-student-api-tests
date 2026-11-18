from src.main.api.fixtures.api_fixture import *
from src.main.api.fixtures.account_fixture import *

import pytest
import allure
import logging

from src.main.api.fixtures.account_fixture import *


@pytest.fixture(autouse=True)
def attach_logs(caplog):
    caplog.set_level(logging.INFO)

    yield

    if caplog.text:
        allure.attach(
            caplog.text,
            name="Test Execution Logs",
            attachment_type=allure.attachment_type.TEXT
        )