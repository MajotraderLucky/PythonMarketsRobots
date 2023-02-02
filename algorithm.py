from binance.client import Client
import keys
import time

# No changed

client = Client(keys.api_key, keys.api_secret)

balance29_12_22 = 13.15539128
balance02_02_23 = 19.12184272
strBalance29_12_22 = "29-12  eq = " + str(balance29_12_22)
strBalance02_02_23 = "02-02  eq = " + str(balance02_02_23)

client = Client(keys.api_key, keys.api_secret)
depth = client.get_order_book(symbol='ETHUSDT')
depthBids = depth['bids']
depthAsks = depth['asks']

futuresDepth = client.futures_order_book(symbol='ETHUSDT')
futBids = futuresDepth['bids']
futAsks = futuresDepth['asks']

balance = client.futures_account_balance()[6]['balance']
printCurrentBalance = "Current balance = " + balance
startBalanceFloat = float(balance)
result = (startBalanceFloat - balance29_12_22)
percentResult = ((result / balance29_12_22) * 100)
printOverallResult = "The percentage overall result = \n     " + \
    str(percentResult) + "%"

startAlgoPrice = futAsks
maxPrice = startAlgoPrice
minPrice = startAlgoPrice
