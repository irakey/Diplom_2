import allure
import pytest
import requests
from data import Urls, ServerAnswers
from helpers import RealUserData, LogInUser

@allure.suite('Проверка авторизации пользователя')
class TestLogInUser:

    @allure.title('Проверка авторизации существующего пользователя')
    def test_log_in_real_user(self):
        user_data = RealUserData.real_user_data()
        response = requests.post(Urls.LOG_IN, data=user_data)
        assert response.json()['success'] is True

    @allure.title('Проверка авторизации нового пользователя')
    @pytest.mark.parametrize('user_data',
                             [
                                 LogInUser.log_in_wrong_email,
                                 LogInUser.log_in_wrong_password
                             ]
                            )
    def test_log_in_user_without_any_fields(self, user_data):
        response = requests.post(Urls.LOG_IN, data=user_data)
        assert 401 == response.status_code and response.json()['message'] == ServerAnswers.unautorized_user
