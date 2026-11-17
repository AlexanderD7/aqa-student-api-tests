from src.main.api.foundation.endpoint import EndpointRequest
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_account_request import CreateAccountRequestModel
from src.main.api.models.create_account_response import CreateAccountResponseModel
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.get_student_response_model import GetStudentResponseModel
from src.main.api.models.get_students_response_model import GetStudentsResponseModel

class AccountSteps(BaseSteps):
    def create_account(self, request: CreateAccountRequestModel) -> CreateAccountResponseModel:
        requester = ValidateCrudRequester(
            request_spec = RequestSpecs.base_headers(),
            endpoint = EndpointRequest.CREATE_ACCOUNT,
            response_spec = ResponseSpecs.request_ok(),
        )
        response_model = requester.post(request)
        self.created_obj.append(response_model.student.id)
        return response_model

    def delete_account(self,student_id: int):
        requester = ValidateCrudRequester(
            request_spec = RequestSpecs.base_headers(),
            endpoint = EndpointRequest.DELETE_ACCOUNT,
            response_spec = ResponseSpecs.request_ok(),
        )
        response_model = requester.delete(student_id = student_id)
        return response_model
    def get_account(self,student_id: int) -> GetStudentResponseModel:
        requester = ValidateCrudRequester(
            request_spec= RequestSpecs.base_headers(),
            endpoint = EndpointRequest.GET_ACCOUNT,
            response_spec = ResponseSpecs.request_ok(),
        )
        response_model = requester.get(student_id = student_id)
        return response_model
    def get_accounts(self) -> GetStudentsResponseModel:
        requester = ValidateCrudRequester(
            request_spec= RequestSpecs.base_headers(),
            endpoint = EndpointRequest.GET_ACCOUNTS,
            response_spec = ResponseSpecs.request_ok(),
        )
        response_model = requester.get()
        return response_model