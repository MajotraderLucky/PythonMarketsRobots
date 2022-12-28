from binance.client import Client
import keys

quantityEth = 0.01
symbolEth = 'ETHUSDT'
client = Client(keys.api_key, keys.api_secret)

# client.futures_cancel_all_open_orders(symbol='ETHUSDT')

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
