import requests
import constants


class TestOrderList:

    def test_order_list_in_response_body(self):
        response = requests.get(constants.BASE_URL + "/api/v1/orders")
        assert response.json()['orders']
