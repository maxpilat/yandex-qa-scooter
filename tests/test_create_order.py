import requests
import pytest
import constants
import allure


class TestCreateOrder:

    @allure.title('Можно создать заказ c указанием цветов {colors}')
    @pytest.mark.parametrize('colors', [['BLACK'], ['BLACK', 'GREY'], []])
    def test_create_order_with_color_options(self, colors):
        response = requests.post(
            constants.ORDERS_URL, json=constants.ORDER_DATA | {"color": colors})
        assert response.status_code == 201 and response.json()['track']
