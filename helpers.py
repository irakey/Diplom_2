from faker import Faker

class CreateRandomUser:

    @staticmethod
    def random_user():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_email():
        faker = Faker('ru_RU')
        user = {
            'email': '',
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_password():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': '',
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_name():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': ''
        }
        return user

class RandomUserWithoutFields(CreateRandomUser):
    user_without_email = CreateRandomUser.create_random_user_without_email()
    user_without_password = CreateRandomUser.create_random_user_without_password()
    user_without_name = CreateRandomUser.create_random_user_without_name()
class RealUserData:

    @staticmethod
    def registrated_user():
        user = {
            'email': 'samarskiy@ya.com',
            'password': '123456qwe',
            'name': 'Sasha'
        }
        return user


    @staticmethod
    def real_user_data():
        user = {
            'email': 'samarskiy@ya.com',
            'password': '123456qwe',
        }
        return user

    @staticmethod
    def wrong_email():
        user = {
            'email': 'samarskiy@ya.com',
            'password': '12345644wet',
        }
        return user

    @staticmethod
    def wrong_password():
        user = {
            'email': 'samarskiy@ya.com',
            'password': '55dwgqwe',
        }
        return user

class LogInUser:
    log_in_wrong_email = RealUserData.wrong_email()
    log_in_wrong_password = RealUserData.wrong_password()