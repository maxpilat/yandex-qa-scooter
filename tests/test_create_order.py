import requests
import pytest
import constants
import allure


class TestCreateOrder:

    @allure.title('Можно создать заказ c указанием цветов {colors}')
    @pytest.mark.parametrize('colors', [['BLACK'], ['BLACK', 'GREY'], []])
    def test_create_order_with_color_options(self, colors):
        response = requests.post(
            constants.BASE_URL + "/api/v1/orders", json=constants.ORDER_DATA | {"color": colors})
        assert response.status_code == 201

    @allure.title('При создании заказа тело ответа содержит track')
    def test_create_order_returns_track(self):
        response = requests.post(
            constants.BASE_URL + "/api/v1/orders", json=constants.ORDER_DATA)
        assert response.json()['track']
