import requests
from http import HTTPStatus

class ResponseSpecs:

    @staticmethod
    def request_ok():
        def confirm(response: requests.Response):
            assert response.status_code == HTTPStatus.OK, response.text
        return confirm

    @staticmethod
    def request_bad():
        def confirm(response: requests.Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST, response.text

        return confirm

    @staticmethod
    def request_unprocessable():
        def confirm(response: requests.Response):
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, response.text

        return confirm