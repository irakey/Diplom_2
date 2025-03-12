import allure
import requests
from data import Urls, Ingredients, ServerAnswers

@allure.suite('Проверка создания заказа')
class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_autorized_user(self, create_user):
        user_data = create_user
        response = requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        create_order = requests.post(Urls.CREATE_ORDER, data=data, headers={
            'Authorization': f'{response.json()['accessToken']}'})
        assert create_order.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_unautorized_user(self, create_user):
        user_data = create_user
        requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        create_order = requests.post(Urls.CREATE_ORDER, data=data)
        assert create_order.json()['success'] is True

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_wrong_ingredient(self, create_user):
        user_data = create_user
        requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': [Ingredients.BUN_SHAO_KAN]}
        create_order = requests.post(Urls.CREATE_ORDER, data=data)
        assert 500 == create_order.status_code

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_without_ingredient(self, create_user):
        user_data = create_user
        requests.post(Urls.CREATE, data=user_data)
        data = {'ingredients': ['']}
        create_order = requests.post(Urls.CREATE_ORDER, data=data)
        assert 400 == create_order.status_code and create_order.json()['message'] == ServerAnswers.no_ingredient