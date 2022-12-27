from binance.client import Client
import keys
# import pandas as pd

balance27_12_22 = -0.1722

client = Client(keys.api_key, keys.api_secret)
depth = client.get_order_book(symbol='ETHUSDT')
depthBids = depth['bids']
depthAsks = depth['asks']
print("****This is spot spread****")
print("---------------------------")
print(depthAsks[0][0], "-", depthAsks[0][1])
print("---------------------------")
print(depthBids[0][0], "-", depthBids[0][1])
print("---------------------------")
print("---------------------------")
print("---------------------------")

futuresDepth = client.futures_order_book(symbol='ETHUSDT')
futBids = futuresDepth['bids']
futAsks = futuresDepth['asks']
print("***This is futures spread**")
print("---------------------------")
print(futAsks[0][0], "-", futAsks[0][1])
print("---------------------------")
print(futBids[0][0], "-", futBids[0][1])
print("---------------------------")
print("---------------------------")

balance = client.futures_account_balance()[6]['balance']
startBalanceFloat = float(balance)
print(startBalanceFloat)

symbolEth = 'ETHUSDT'
quantityEth = 0.01
interval = '5m'

# ----------BUY_MARKET_ORDER---------------

# buy_market = client.futures_create_order(
#     symbol='ETHUSDT',
#     side='BUY',
#     type='MARKET',
#     quantity=quantityEth)

# takeBuyMarket = client.futures_create_order(
#     symbol=symbolEth,
#     side="SELL",
#     type="TAKE_PROFIT_MARKET",
#     stopPrice='1225',
#     closePosition="true")

# stopBuy = client.futures_create_order(
#     symbol=symbolEth,
#     side="SELL",
#     type="STOP_MARKET",
#     stopPrice='1205',
#     closePosition="true")

# takeBuyLimit = client.futures_create_order(
#     symbol=symbolEth,
#     side="SELL",
#     type="LIMIT",
#     quantity=quantityEth,
#     price='1225',
#     timeInForce="GTC")

# ----------------------------------------

# sell_market = client.futures_create_order(
#     symbol='ETHUSDT',
#     side='SELL',
#     type='MARKET',
#     quantity=0.01)

# openShortLimit = client.futures_create_order(
#     symbol=symbolEth,
#     side="SELL",
#     type="LIMIT",
#     quantity=quantityEth,
#     price='1225',
#     timeInForce="GTC")

Client.KLINE_INTERVAL_5MINUTE
klines = client.get_historical_klines(symbolEth, interval, "26 Dec,2021")
print(klines)
# data = pd.DataFrame(klines)
