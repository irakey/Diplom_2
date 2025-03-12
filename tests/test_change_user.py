import allure
import pytest
import requests
from data import Urls, ServerAnswers
from helpers import CreateRandomUser

@allure.suite('Проверка изменения данных пользователя')
class TestChangeUser:

    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
                                             ({'email: faker.email()'}),
                                             ({'password: faker.password()'}),
                                             ({'name: faker.name()'})
                                            ]
                            )
    def test_change_autorized_user(self, update_data, create_user):
        user_data = create_user
        response = requests.post(Urls.CREATE, data=user_data)
        new_data = requests.patch(Urls.UPDATE_USER,
                                data=update_data, headers={'Authorization': f'{response.json()['accessToken']}'})
        assert new_data.json()['success'] is True

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
                                             ({'email: faker.email()'}),
                                             ({'password: faker.password()'}),
                                             ({'name: faker.name()'})
                                            ]
                             )
    def test_change_unautorized_user(self, update_data):
        user_data = CreateRandomUser.random_user()
        requests.post(Urls.CREATE, data=user_data)
        new_data = requests.patch(Urls.UPDATE_USER,
                                  data=update_data, headers={'Authorization': None})
        assert 401 == new_data.status_code and new_data.json()['message'] == ServerAnswers.no_token