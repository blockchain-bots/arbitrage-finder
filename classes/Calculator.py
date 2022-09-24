"""
Calculator class
"""


class Calculator:
    def __init__(self, exchanges):
        """Define Calculator variables"""

        self.exchanges = exchanges
        self.cheapest_exchange = None
        self.expensive_exchange = None

    def set_exchange_prices(self):
        """Retrieve all prices from exchanges"""

        for exchange in self.exchanges:
            exchange.set_btc_eur_price()

    def find_arbitrage(self):
        """Find arbitrage by finding highest and lowest price from exchanges"""

        self.cheapest_exchange = self.find_cheapest_exchange()
        self.expensive_exchange = self.find_expensive_exchange()

    def calc_arbitrage_percentage(self):
        """Calculate arbitrage percentage difference"""

        cheapest_price = self.cheapest_exchange.btc_eur_price
        expensive_price = self.expensive_exchange.btc_eur_price

        if cheapest_price is None or expensive_price is None:
            return print("No arbitrage found (yet)")

        if cheapest_price == expensive_price:
            return 100.0
        try:
            return (abs(cheapest_price - expensive_price) / expensive_price) * 100.0
        except ZeroDivisionError:
            return 0

    def calc_arbitrage_price(self):
        """Calculate arbitrage price difference"""

        cheapest_price = self.cheapest_exchange.btc_eur_price
        expensive_price = self.expensive_exchange.btc_eur_price

        if cheapest_price is None or expensive_price is None:
            return print("No arbitrage found (yet)")

        return expensive_price - cheapest_price

    def find_cheapest_exchange(self):
        """Find exchange with the lowest price"""

        price = None
        exchange = None
        for exchange_item in self.exchanges:
            if price is None or price > exchange_item.btc_eur_price:
                price = exchange_item.btc_eur_price
                exchange = exchange_item

        return exchange

    def find_expensive_exchange(self):
        """Find exchange with the highest price"""

        price = None
        exchange = None
        for exchange_item in self.exchanges:
            if price is None or price < exchange_item.btc_eur_price:
                price = exchange_item.btc_eur_price
                exchange = exchange_item

        return exchange
