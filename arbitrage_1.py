"""
Crypto arbitrage finder bot
"""
from classes.Calculator import Calculator
from classes.Exchange import Exchange

if __name__ == "__main__":
    exchanges = [
        Exchange("Bitvavo", "https://api.bitvavo.com/v2/ticker/price?market=BTC-EUR"),
        Exchange("Binance", "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR"),
        Exchange("Coinbase", "https://api.exchange.coinbase.com/products/BTC-EUR/ticker")
    ]

    calculator = Calculator(exchanges)
    calculator.set_exchange_prices()
    calculator.find_arbitrage()

    for exchange in calculator.exchanges:
        print(exchange.name + ": €" + str(exchange.btc_eur_price) + ",-")

    print("\nHIGH: " + calculator.expensive_exchange.name)
    print("LOW: " + calculator.cheapest_exchange.name)
    print("\nPercentage: " + str(calculator.calc_arbitrage_percentage()) + "%")
    print("Price difference: €" + str(calculator.calc_arbitrage_price()) + ",-")
