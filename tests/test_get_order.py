import allure
import requests
from data import Urls, Ingredients, ServerAnswers

@allure.suite('Проверка получения заказов пользователя')
class TestGetOrder:

    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_order_autorized_user(self, create_user):
        user_data = create_user
        response = requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        requests.post(Urls.CREATE_ORDER, data=data, headers={
            'Authorization': f'{response.json()['accessToken']}'})
        get_order = requests.get(Urls.GET_ORDER, data=user_data, headers={
            'Authorization': f'{response.json()['accessToken']}'})
        assert get_order.json()['success'] is True

    @allure.title('Проверка получения заказов  не авторизованного пользователя')
    def test_create_order_unautorized_user(self, create_user):
        user_data = create_user
        requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        requests.post(Urls.CREATE_ORDER, data=data)
        get_order = requests.get(Urls.GET_ORDER, data=user_data)
        assert 401 == get_order.status_code and get_order.json()['message'] == ServerAnswers.without_autorization