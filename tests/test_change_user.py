import allure
import pytest
import requests
from data import Urls, ServerAnswers


@allure.suite('Проверка изменения данных пользователя')
class TestChangeUser:

    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
        {'email': 'faker.email()'},
        {'password': 'faker.password()'},
        {'name': 'faker.name()'}
    ])
    def test_change_autorized_user(self, update_data, authorize_user):
        token = authorize_user
        new_data = requests.patch(
            Urls.UPDATE_USER,
            data=update_data,
            headers={'Authorization': f'{token}'}
        )
        assert new_data.json()['success'] is True

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
        {'email': 'faker.email()'},
        {'password': 'faker.password()'},
        {'name': 'faker.name()'}
    ])
    def test_change_unautorized_user(self, update_data):
        new_data = requests.patch(
            Urls.UPDATE_USER,
            data=update_data,
            headers={'Authorization': None}
        )
        assert new_data.status_code == 401
        assert new_data.json()['message'] == ServerAnswers.no_token
