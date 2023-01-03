from binance.client import Client
import keys
import time

# No changed

client = Client(keys.api_key, keys.api_secret)

balance29_12_22 = 13.15539128
strBalance29_12_22 = "29-12  eq = " + str(balance29_12_22)

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

# while True:
#     if futAsks > startAlgoPrice:
#         maxPrice = futAsks
#         print("New max = ", maxPrice)
#     elif futAsks < startAlgoPrice:
#         minPrice = futAsks
#         print("New min = ", minPrice)

#     time.sleep(10)


# for i in range(30):
#     print(f"", client.futures_order_book(symbol='ETHUSDT')['bids'][0][0])
#     os.system('clear')

# if len(client.futures_get_open_orders()) == 2:
        #     order1 = client.futures_get_open_orders()[0]['price']
        #     order2 = client.futures_get_open_orders()[1]['price']
        #     sideOrder1 = client.futures_get_open_orders()[0]['side']
        #     sideOrder2 = client.futures_get_open_orders()[1]['side']
        #     print(f"Price order #1:", order1)
        #     print(f"Price order #2:", order2)
        #     print(f"Side order #1:", sideOrder1)
        #     print(f"Side order #2:", sideOrder2)
        #     if order1 > order2:
        #         print(f"order1 is a limit:", order1)
