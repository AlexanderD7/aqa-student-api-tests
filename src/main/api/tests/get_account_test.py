import pytest
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel


@allure.epic("Управление студентами")
@allure.feature("GET операции")
class TestGetAccount:
    @allure.title("Получение данных об одном студенте по ID")
    def test_get_student_by_id(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
        @pytest.mark.xfail(reason="BUG-1: API не сохраняет созданных студентов, GET возвращает 'Student not found'")
        @allure.title("Получение данных об одном студенте по ID")
        def test_get_student_by_id(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
            create_response = api_manager.account_steps.create_account(create_account_request)
            student_id = create_response.student.id

            with allure.step(f"Запрос данных студента с ID: {student_id}"):
                get_response = api_manager.account_steps.get_account(student_id)

            assert get_response.status == 1
            assert get_response.student.id == student_id
            assert get_response.student.email == create_account_request.email

    @allure.title("Получение списка всех студентов")
    def test_get_all_students(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
        api_manager.account_steps.create_account(create_account_request)

        get_response = api_manager.account_steps.get_accounts()

        assert get_response.status == 1
        assert isinstance(get_response.students, list)
        assert len(get_response.students) > 0

        first_student = get_response.students[0]
        assert first_student.id > 0
        assert first_student.email is not None
        student_ids = [student.id for student in get_response.students]
        allure.attach(
            str(student_ids),
            name="Список ID всех студентов",
            attachment_type=allure.attachment_type.TEXT
        )

    @pytest.mark.xfail(reason="BUG-1: Созданный студент не появляется в списке")
    @allure.title("Получение списка всех студентов")
    def test_get_all_students(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):

        create_response = api_manager.account_steps.create_account(create_account_request)
        created_student_id = create_response.student.id

        get_response = api_manager.account_steps.get_accounts()

        assert get_response.status == 1
        assert isinstance(get_response.students, list)
        assert len(get_response.students) > 0

        student_ids = [student.id for student in get_response.students]

        assert created_student_id in student_ids, (
            f"Созданный студент с ID {created_student_id} не найден в списке всех студентов! "
            f"Список ID в базе: {student_ids}"
        )