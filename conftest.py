import pytest
import requests
from data import Urls
from helpers import CreateRandomUser


@pytest.fixture
def create_user():
    user_data = CreateRandomUser.random_user()
    yield user_data
    login_user = requests.post(Urls.LOG_IN, data=user_data)
    token = login_user.json()['accessToken']
    requests.delete(Urls.UPDATE_USER, headers={'Authorization': token})


@pytest.fixture
def authorize_user(create_user):
    login_user = requests.post(Urls.LOG_IN, data=create_user)
    token = login_user.json()['accessToken']
    return token