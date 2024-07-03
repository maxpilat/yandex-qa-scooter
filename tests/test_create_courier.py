import requests
from utils import register_new_courier_and_return_login_password
import constants
import allure


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        assert courier_data

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.BASE_URL + "/api/v1/courier", data={
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        })
        assert response.status_code == 409

    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_courier_with_error_params(self):
        response = requests.post(constants.BASE_URL + "/api/v1/courier", data={
            "password": "password",
            "firstName": "firstName"
        })
        assert response.status_code == 400

    @allure.title('Запрос возвращает правильный код ответа')
    def test_create_courier_returns_correct_status_code(self):
        response = register_new_courier_and_return_login_password()[1]
        assert response.status_code == 201

    @allure.title('Успешный запрос возвращает ok: true')
    def test_create_courier_returns_ok_on_success(self):
        response = register_new_courier_and_return_login_password()[1]
        assert response.json()['ok']
