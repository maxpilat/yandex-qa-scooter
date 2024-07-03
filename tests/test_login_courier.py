import requests
from utils import register_new_courier_and_return_login_password
import constants


class TestLoginCourier:

    def test_courier_login_successful(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.BASE_URL + "/api/v1/courier/login", data={
            "login": courier_data[0],
            "password": courier_data[1],
        })
        assert response.status_code == 200

    def test_login_courier_with_error_params(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.BASE_URL + "/api/v1/courier/login", data={
            "password": courier_data[1],
        })
        assert response.status_code == 400

    def test_courier_login_nonexistent_user_error(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.BASE_URL + "/api/v1/courier/login", data={
            "login": "nonexistent_user",
            "password": courier_data[1],
        })
        assert response.status_code == 404

    def test_courier_login_returns_id(self):
        courier_data = register_new_courier_and_return_login_password()[0]
        response = requests.post(constants.BASE_URL + "/api/v1/courier/login", data={
            "login": courier_data[0],
            "password": courier_data[1],
        })
        assert response.json()['id']
