from binance.client import Client
import keys
import setupPosition
import algorithm
import time
import os

client = Client(keys.api_key, keys.api_secret)

print("****This is spot spread****")
print("---------------------------")
print(algorithm.depthAsks[0][0], "-", algorithm.depthAsks[0][1])
print("---------------------------")
print(algorithm.depthBids[0][0], "-", algorithm.depthBids[0][1])
print("---------------------------")
print("---------------------------")

print("***This is futures spread**")
print("---------------------------")
print("    ", algorithm.futAsks[0][0], "-", algorithm.futAsks[0][1])
print("---------------------------")
print("    ", algorithm.futBids[0][0], "-", algorithm.futBids[0][1])
print("---------------------------")
print("---------------------------")
print(algorithm.printCurrentBalance)
print(algorithm.printOverallResult)


while True:
    for i in range(10, 0, -1):
        print(f"Waiting: {i:2} cicles.")
        print(f"", client.futures_order_book(symbol='ETHUSDT')['bids'][0][0])
        a = client.futures_order_book(symbol='ETHUSDT')['bids'][0][0]
        print(f"", a)
        time.sleep(15)
        os.system("clear")
