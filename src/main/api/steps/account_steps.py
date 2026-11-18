import allure
from src.main.api.foundation.endpoint import EndpointRequest
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_account_request import CreateAccountRequestModel
from src.main.api.models.create_account_response import CreateAccountResponseModel
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.get_student_response_model import GetStudentResponseModel
from src.main.api.models.get_students_response_model import GetStudentsResponseModel
from src.main.api.models.update_account_request_model import UpdateAccountRequestModel
from src.main.api.models.update_account_response_model import UpdateAccountResponseModel
from src.main.api.foundation.requesters.crud_requester import CrudRequester


class AccountSteps(BaseSteps):

    @allure.step("Создание студента")
    def create_account(self, request: CreateAccountRequestModel) -> CreateAccountResponseModel:
        requester = ValidateCrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.CREATE_ACCOUNT,
            response_spec=ResponseSpecs.request_ok(),
        )
        response_model = requester.post(request)

        allure.attach(
            f"Создан студент:\nID: {response_model.student.id}\nEmail: {response_model.student.email}",
            name="Данные созданного студента",
            attachment_type=allure.attachment_type.TEXT
        )
        self.created_obj.append(response_model.student.id)
        return response_model

    @allure.step("Удаление студента с ID: {student_id}")
    def delete_account(self, student_id: int):
        requester = ValidateCrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.DELETE_ACCOUNT,
            response_spec=ResponseSpecs.request_ok(),
        )
        response_model = requester.delete(student_id=student_id)
        return response_model

    @allure.step("Получение данных студента с ID: {student_id}")
    def get_account(self, student_id: int) -> GetStudentResponseModel:
        requester = ValidateCrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.GET_ACCOUNT,
            response_spec=ResponseSpecs.request_ok(),
        )
        response_model = requester.get(student_id=student_id)
        return response_model

    @allure.step("Получение списка всех студентов")
    def get_accounts(self) -> GetStudentsResponseModel:
        requester = ValidateCrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.GET_ACCOUNTS,
            response_spec=ResponseSpecs.request_ok(),
        )
        response_model = requester.get()
        return response_model

    @allure.step("Обновление данных студента с ID: {student_id}")
    def update_account(self, student_id: int, request: UpdateAccountRequestModel) -> UpdateAccountResponseModel:
        requester = ValidateCrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.PUT_ACCOUNT_UPDATE,
            response_spec=ResponseSpecs.request_ok(),
        )
        response_model = requester.put(request, student_id=student_id)

        allure.attach(
            f"Студент обновлен:\nID: {response_model.student.id}\nНовое имя: {response_model.student.name}",
            name="Данные обновленного студента",
            attachment_type=allure.attachment_type.TEXT
        )
        return response_model

    @allure.step("Попытка создания студента с невалидными данными")
    def create_invalid_account(self, request: CreateAccountRequestModel):
        requester = CrudRequester(
            request_spec=RequestSpecs.base_headers(),
            endpoint=EndpointRequest.CREATE_ACCOUNT,
            response_spec=ResponseSpecs.request_bad(),
        )
        return requester.post(request)