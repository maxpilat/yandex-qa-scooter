import requests
from utils import register_new_courier_and_return_login_password
import constants
import allure


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_courier_login_successful(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.COURIER_LOGIN_URL, data={
            "login": courier_data[0],
            "password": courier_data[1],
        })
        assert response.status_code == 200 and response.json()['id']

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_courier_with_error_params(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.COURIER_LOGIN_URL, data={
            "password": courier_data[1],
        })
        assert response.status_code == 400 and response.json(
        )['message'] == "Недостаточно данных для входа"

    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_courier_login_nonexistent_user_error(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.COURIER_LOGIN_URL, data={
            "login": "nonexistent_user",
            "password": courier_data[1],
        })
        assert response.status_code == 404 and response.json(
        )['message'] == "Учетная запись не найдена"
