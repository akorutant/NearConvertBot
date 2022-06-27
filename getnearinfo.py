import requests


class NearInfo:
    def __init__(self, api_key):
        self.url_near = "https://rest.coinapi.io/v1/exchangerate/NEAR?filter_asset_id=USD;BYN;RUB"
        self.headers = {'X-CoinAPI-Key': api_key}

    def get_near_info(self):
        response = requests.get(self.url_near, headers=self.headers)
        response = response.json()
        return response
