"""
Exchange class
"""
import requests


class Exchange:
    def __init__(self, name, api):
        """Define exchange variables"""

        self.name = name
        self.api = api
        self.btc_eur_price = None

    def set_btc_eur_price(self):
        """Get price from exchange data"""

        response = requests.get(self.api, timeout=5)
        json_response = response.json().items()

        for key, value in json_response:
            if key == "price":
                self.btc_eur_price = float(value)
