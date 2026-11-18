import pytest
import allure
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_request import CreateAccountRequestModel


@allure.epic("Управление студентами")
@allure.feature("GET операции")
class TestGetAccount:
    @pytest.mark.xfail(reason="BUG-1: API не сохраняет созданных студентов")
    @allure.title("Получение данных об одном студенте по ID")
    def test_get_student_by_id(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
        create_response = api_manager.account_steps.create_account(create_account_request)
        student_id = create_response.student.id

        with allure.step(f"Запрос данных студента с ID: {student_id}"):
            get_response = api_manager.account_steps.get_account(student_id)

        assert get_response.status == 1, f"Не удалось получить студента с ID: {student_id}. Статус: {get_response.status}"
        assert get_response.student.id == student_id, f"Пришел неверный ID! Ожидали {student_id}, получили {get_response.student.id}"

    @pytest.mark.xfail(reason="BUG-1: Созданный студент не появляется в списке (Eventual Consistency)")
    @allure.title("Проверка наличия созданного студента в списке всех студентов")
    def test_get_all_students(self, api_manager: ApiManager, create_account_request: CreateAccountRequestModel):
        create_response = api_manager.account_steps.create_account(create_account_request)
        created_student_id = create_response.student.id

        get_response = api_manager.account_steps.get_accounts()

        assert get_response.status == 1
        assert isinstance(get_response.students, list)
        assert len(get_response.students) > 0

        student_ids = [student.id for student in get_response.students]
        allure.attach(
            str(student_ids),
            name="Список ID всех студентов",
            attachment_type=allure.attachment_type.TEXT
        )

        assert created_student_id in student_ids, (
            f"Созданный студент с ID {created_student_id} не найден в списке всех студентов! "
            f"Список ID в базе: {student_ids}"
        )