# https://blog.coinfabrik.com/finance/what-i-have-learned-from-my-arbitrage-experiences-with-cryptoassets/
import numpy as np
import ccxt

exchanges = ["Binance", "Bitfinex", "Bittrex", "Cex", "Exmo", "Hitbtc", "Huobipro", "Kraken", "Kucoin", "Okex",
             "Poloniex", "Yobit"]

clients = [getattr(ccxt, e.lower())() for e in exchanges]

symbols = ["ADA/BTC", "BCH/BTC", "BTG/BTC", "BTS/BTC", "CLAIM/BTC", "DASH/BTC", "DOGE/BTC", "EDO/BTC", "EOS/BTC",
           "ETC/BTC", "ETH/BTC", "FCT/BTC", "ICX/BTC", "IOTA/BTC", "LSK/BTC", "LTC/BTC", "MAID/BTC", "NEO/BTC",
           "OMG/BTC", "QTUM/BTC", "STR/BTC", "TRX/BTC", "VEN/BTC", "XEM/BTC", "XLM/BTC", "XMR/BTC", "XRP/BTC",
           "ZEC/BTC"]

ask = np.zeros((len(symbols), len(clients)))
bid = np.zeros((len(symbols), len(clients)))

for row, symbol in enumerate(symbols):
    for col, client in enumerate(clients):
        book = client.fetch_order_book(symbol)
        ask[row, col] = book['asks'][0][0]
        bid[row, col] = book['bids'][0][0]

fee = 0.25

opportunities = []

for i, symbol in enumerate(symbols):
    for j1, exchange1 in enumerate(exchanges):
        for j2, exchange2 in enumerate(exchanges):

            roi = 0
            if j1 != j2 and ask[i, j1] > 0:
                roi = ((bid[i, j2] * (1 - fee / 100)) / (ask[i, j1] * (1 + fee / 100)) - 1) * 100

                if roi > 0:
                    opportunities.append([symbol, exchange1, ask[i, j1], exchange2, bid[i, j2], round(roi, 2)])

print("Number of profitable opportunities:", len(opportunities))

opportunities = sorted(opportunities, reverse=True, key=lambda x: x[5])
for opp in opportunities[:10]:
    print(opp)
