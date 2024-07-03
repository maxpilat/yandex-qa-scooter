import requests
import pytest
import constants


class TestCreateCourier:

    @pytest.mark.parametrize('colors', [['BLACK'], ['BLACK', 'GREY'], []])
    def test_create_order_with_color_options(self, colors):
        response = requests.post(constants.BASE_URL + "/api/v1/orders", json={
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colors
        })
        assert response.status_code == 201

    def test_create_order_returns_track(self):
        response = requests.post(constants.BASE_URL + "/api/v1/orders", json={
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        })
        assert response.json()['track']
