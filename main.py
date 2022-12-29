from binance.client import Client
import keys
import setupPosition
import algorithm
import time
import os

client = Client(keys.api_key, keys.api_secret)
symbolEth = 'ETHUSDT'
startPrice = client.futures_order_book(
    symbol=symbolEth)['asks'][0][0]
priceArr = []
maxArr = []
list_uniq_max_arr = []

while True:
    for i in range(10, 0, -1):
        print(f"------------------------")
        print(f" --Waiting:{i:2} cicles--")
        futBidPrise = "BID: " + client.futures_order_book(
            symbol='ETHUSDT')['bids'][0][0] + " - " + client.futures_order_book(
            symbol='ETHUSDT')['bids'][0][1]
        futAskPrise = "ASK: " + client.futures_order_book(
            symbol='ETHUSDT')['asks'][0][0] + " - " + client.futures_order_book(
            symbol='ETHUSDT')['asks'][0][1]
        spotAskPrice = "ASK: " + client.get_order_book(
            symbol=symbolEth)['asks'][0][0]
        volumeAskPrice = "Volume ask: " + client.get_order_book(
            symbol=symbolEth)['asks'][0][1]
        spotBidPrice = "BID: " + client.get_order_book(
            symbol=symbolEth)['bids'][0][0]
        volumeBidPrice = "Volume bid: " + client.get_order_book(
            symbol=symbolEth)['bids'][0][1]
        futBalanceNow = client.futures_account_balance()[6]['balance']
        profit = float(futBalanceNow) - algorithm.balance29_12_22
        profitPercent = (profit / algorithm.balance29_12_22) * 100
        floatFutAskPrice = float(client.futures_order_book(
            symbol=symbolEth)['asks'][0][0])
        priceArr.append(floatFutAskPrice)
        maxPrice = max(priceArr)
        minPrice = min(priceArr)

        print(f"------------------------")
        print(f"----------spot----------")
        print(f"------------------------")
        print(f"", spotAskPrice)
        print(f"", volumeAskPrice)
        print(f"", spotBidPrice)
        print(f"", volumeBidPrice)
        print(f"------------------------")
        print(f"---------futures--------")
        print(f"------------------------")
        print(f"", futAskPrise)
        print(f"", futBidPrise)
        print(f"------------------------")
        print(f"", algorithm.strBalance29_12_22)
        print(f"Equity now =", futBalanceNow)
        print(f"My profit  =", str(profit) + "$")
        print(f"Profit %   =", str(profitPercent) + "%")
        print(f"------------------------")
        print(f"Start price -", startPrice)
        print(f"", priceArr)
        print(f"high =", maxPrice)
        print(f"low  =", minPrice)
        time.sleep(20)
        os.system("clear")
