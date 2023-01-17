import sys

from binance.client import Client
import keys
import time
import os
import algorithm

client = Client(keys.api_key, keys.api_secret)
symbolETH = 'ETHUSDT'
symbolBTC = 'BTCUSDT'
startPrice = client.futures_order_book(
    symbol=symbolBTC)['asks'][0][0]
priceArr = []
maxArr = []
minArr = []
while True:
    for i in range(10, 0, -1):
        print(f"------------------------")
        print(f" --Waiting:{i:2} cicles--")
        futBidPrise = "BID: " + client.futures_order_book(
            symbol=symbolBTC)['bids'][0][0] + " - " + client.futures_order_book(
            symbol=symbolBTC)['bids'][0][1]
        futAskPrise = "ASK: " + client.futures_order_book(
            symbol=symbolBTC)['asks'][0][0] + " - " + client.futures_order_book(
            symbol=symbolBTC)['asks'][0][1]
        spotAskPrice = "ASK: " + client.get_order_book(
            symbol=symbolBTC)['asks'][0][0]
        volumeAskPrice = "Volume ask: " + client.get_order_book(
            symbol=symbolBTC)['asks'][0][1]
        spotBidPrice = "BID: " + client.get_order_book(
            symbol=symbolBTC)['bids'][0][0]
        volumeBidPrice = "Volume bid: " + client.get_order_book(
            symbol=symbolBTC)['bids'][0][1]
        futBalanceNow = client.futures_account_balance()[6]['balance']
        profit = float(futBalanceNow) - algorithm.balance29_12_22
        profitPercent = (profit / algorithm.balance29_12_22) * 100
        floatFutAskPrice = float(client.futures_order_book(
            symbol=symbolBTC)['asks'][0][0])
        priceArr.append(floatFutAskPrice)
        maxPrice = max(priceArr)
        minPrice = min(priceArr)
        maxArr.append(maxPrice)
        minArr.append(minPrice)
        difference = round((maxPrice - minPrice), 2)
        start2max = round((maxPrice - float(startPrice)), 2)
        start2min = round((float(startPrice) - minPrice), 2)
        upTrand = False
        downTrand = False
        if start2max > start2min:
            upTrand = True
            downTrand = False
        elif start2max < start2min:
            downTrand = True
            upTrand = False
        else:
            downTrand = False
            upTrand = False
        # ---------------Fibo short setups----------------------
        shortFib236 = minPrice + ((maxPrice - minPrice) * 0.236)
        shortFib382 = minPrice + ((maxPrice - minPrice) * 0.382)
        shortFib500 = minPrice + ((maxPrice - minPrice) * 0.500)
        shortFib618 = minPrice + ((maxPrice - minPrice) * 0.618)
        shortFib786 = minPrice + ((maxPrice - minPrice) * 0.786)
        # -----------------Fibo long setups---------------------
        longFib236 = maxPrice - ((maxPrice - minPrice) * 0.236)
        longFib382 = maxPrice - ((maxPrice - minPrice) * 0.382)
        longFib500 = maxPrice - ((maxPrice - minPrice) * 0.500)
        longFib618 = maxPrice - ((maxPrice - minPrice) * 0.618)
        longFib786 = maxPrice - ((maxPrice - minPrice) * 0.786)
        # ------------------------------------------------------
        howManyOpenOrders = len(client.futures_get_open_orders())
        setupForLong = upTrand == True and downTrand == False and start2max > 50
        setupForShort = downTrand == True and upTrand == False and start2min > 50
        allOpenOrders = len(client.futures_get_open_orders(symbol=symbolBTC))
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
        # print(f"PriceArr:", priceArr)
        print(f"high =", maxPrice)
        print(f"low  =", minPrice)
        # print(f"MaxArr:", maxArr[1:])
        # print(f"MinArr:", minArr[1:])
        print(f"Difference:", difference)
        print(f"Start to maximum:", start2max)
        print(f"Start to minimum:", start2min)
        print(f"Uptrand:", upTrand)
        print(f"Downtrand:", downTrand)
        print(f"shortFib236:", round(shortFib236, 1))
        print(f"shortFib382:", round(shortFib382, 1))
        print(f"shortFib500:", round(shortFib500, 1))
        print(f"shortFib618:", round(shortFib618, 1))
        print(f"shortFib786:", round(shortFib786, 1))
        print(f"------------------------")
        print(f"longFib236: ", round(longFib236, 1))
        print(f"longFib382: ", round(longFib382, 1))
        print(f"longFib500: ", round(longFib500, 1))
        print(f"longFib618: ", round(longFib618, 1))
        print(f"longFib786: ", round(longFib786, 1))
        print(f"------------------------")
        print(f"Last max =", maxArr[-1])
        print(f"Last min =", minArr[-1])
        print(f"All open wait orders:", allOpenOrders)
        priceLong236 = round(longFib236, 1)
        strPrice236 = str(priceLong236)
        priceLong382 = round(longFib382, 1)
        strPrice382 = str(priceLong382)
        priceShort382 = round(shortFib382, 1)
        strPriceShort382 = str(priceShort382)
        priceLong786 = round(longFib786, 1)
        strPriceLong786 = str(priceLong786)
        priceShort786 = round(shortFib786, 1)
        strPriceShort786 = str(priceShort786)
        priceLong618 = round(longFib618, 1)
        strPriceLong618 = str(priceLong618)
        priceShort618 = round(shortFib618, 1)
        strPriceShort618 = str(priceShort618)
        priceShort236 = round(shortFib236, 1)
        strPriceShort236 = str(priceShort236)
        sizeOpenPosition = next(obj for obj in client.futures_account()[
                                'positions'] if obj['symbol'] == symbolBTC)['positionAmt']
        floatSizeOpenPositions = float(sizeOpenPosition)
        print(f"Size open positions", sizeOpenPosition)
        print(f"float open positions:", floatSizeOpenPositions)
        conditionCreateStopLossLongOrder = allOpenOrders == 0
        conditionOpenLongPosition = (
            setupForLong == True) and len(priceArr) > 10
        conditonOpenShortPositon = setupForShort == True and len(
            priceArr) > 10
        newHigh = (len(maxArr) > 10 and len(minArr) >
                   10) and maxArr[-1] > maxArr[-2]
        newLow = (len(maxArr) > 10 and len(minArr) >
                  10) and minArr[-1] < minArr[-2]
        newExtreme = newHigh == True or newLow == True
        priceLongOpenPosition = 0.0
        priceShortOpenPosition = 0.0
        if conditionOpenLongPosition:
            if priceArr[-1] > priceLong382 and floatSizeOpenPositions == 0.0 and allOpenOrders == 0:
                openLongLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="BUY",
                    type="LIMIT",
                    quantity=0.001,
                    price=strPrice382,
                    timeInForce="GTC"
                )
                priceLongOpenPosition = priceLong382
            if allOpenOrders == 0 and floatSizeOpenPositions > 0.0:
                stopLossBuy = client.futures_create_order(
                    symbol=symbolBTC,
                    side="SELL",
                    type="STOP_MARKET",
                    stopPrice=str(minPrice - 5),
                    closePosition="true"
                )
            if allOpenOrders == 1 and floatSizeOpenPositions > 0.0:
                takeBuyMarket = client.futures_create_order(
                    symbol=symbolBTC,
                    side="SELL",
                    type="TAKE_PROFIT_MARKET",
                    stopPrice=str(maxPrice + 5),
                    closePosition="true"
                )
            elif priceArr[-1] > priceLong618 and floatSizeOpenPositions == 0.001 and allOpenOrders == 2:
                openLongLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="BUY",
                    type="LIMIT",
                    quantity=0.001,
                    price=strPriceLong618,
                    timeInForce="GTC"
                )
            elif priceArr[-1] < priceLong382 and floatSizeOpenPositions == 0.002 and allOpenOrders == 2:
                takeBuyLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="SELL",
                    type="TAKE_PROFIT_MARKET",
                    stopPrice=strPrice236,
                    closePosition="true"
                )
        elif conditonOpenShortPositon:
            if priceArr[-1] < priceShort382 and floatSizeOpenPositions == 0.0 and allOpenOrders == 0:
                openShortLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="SELL",
                    type="LIMIT",
                    quantity=0.001,
                    price=strPriceShort382,
                    timeInForce="GTC"
                )
                priceShortOpenPosition = priceShort382
            if allOpenOrders == 0 and floatSizeOpenPositions < 0.0:
                stopLossSell = client.futures_create_order(
                    symbol=symbolBTC,
                    side="BUY",
                    type="STOP_MARKET",
                    stopPrice=str(maxPrice + 5),
                    closePosition="true"
                )
            if allOpenOrders == 1 and floatSizeOpenPositions < 0.0:
                takeSellMarket = client.futures_create_order(
                    symbol=symbolBTC,
                    side="BUY",
                    type="TAKE_PROFIT_MARKET",
                    stopPrice=str(minPrice - 5),
                    closePosition="true"
                )
            elif priceArr[-1] < priceShort618 and floatSizeOpenPositions == 0.001 and allOpenOrders == 2:
                openShortLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="SELL",
                    type="LIMIT",
                    quantity=0.001,
                    price=strPriceShort618,
                    timeInForce="GTC"
                )
            elif priceArr[-1] > priceShort382 and floatSizeOpenPositions == 0.002 and allOpenOrders == 2:
                takeSellLimit = client.futures_create_order(
                    symbol=symbolBTC,
                    side="BUY",
                    type="TAKE_PROFIT_MARKET",
                    stopPrice=strPriceShort236,
                    closePosition="true"
                )
        if newExtreme and floatSizeOpenPositions == 0:
            client.futures_cancel_all_open_orders(symbol=symbolBTC)
        print(f"Quantity elements priceArr:", len(priceArr))
        conditionRestart = len(
            priceArr) > 1000 and floatSizeOpenPositions == 0.0
        if conditionRestart:
            client.futures_cancel_all_open_orders(symbol=symbolBTC)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        time.sleep(20)
        os.system("clear")
