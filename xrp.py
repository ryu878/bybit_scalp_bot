import ta
import time
import ccxt
import config
import pandas as pd
from pybit import HTTP


exchange = ccxt.bybit({'apiKey': config.api_key,'secret': config.api_secret})
client = HTTP(api_key=config.api_key,api_secret=config.api_secret)
qty1 = config.qty1
maxq = config.maxq

##########################
symbol = 'XRPUSDT'
##########################

decimals = 4

def getOrderBook():
    global ask
    global bid
    orderbook = exchange.fetchOrderBook(symbol=symbol,limit=10)
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None

def get_6ema():
    bars = exchange.fetchOHLCV(symbol=symbol,timeframe = '1m',limit=18)
    df = pd.DataFrame(bars,columns=['Time','Open','High','Low','Close','Vol'])
    df['EMA 6 High'] = ta.trend.EMAIndicator(df['High'], window=6).ema_indicator()
    df['EMA 6 Low'] = ta.trend.EMAIndicator(df['Low'], window=6).ema_indicator()
    global ema6hgh
    global ema6low
    ema6hgh = df['EMA 6 High'][17]
    ema6low = df['EMA 6 Low'][17]
    ema6hgh = round(ema6hgh,decimals)
    ema6low = round(ema6low,decimals)

def get_60ema():
    bars = exchange.fetchOHLCV(symbol=symbol,timeframe = '1m',limit=180)
    df = pd.DataFrame(bars,columns=['Time','Open','High','Low','Close','Vol'])
    df['EMA 60 Close'] = ta.trend.EMAIndicator(df['Close'], window=60).ema_indicator()
    global ema60
    ema60 = df['EMA 60 Close'][179]
    ema60 = round(ema60,decimals)

def get_position():
    positions = client.my_position(symbol=symbol)
    for position in positions['result']:
        if position['side'] == 'Sell':
            global sell_position_size
            global sell_position_prce
            sell_position_size = position['size']
            sell_position_prce = position['entry_price']  

def get_buy_order():
    orders = client.get_active_order(symbol=symbol, limit=21)

    for order in orders['result']['data']:

        global tp_order
        global buy_order_size
        global buy_order_id
        tp_order = order['order_status'] == 'New' and order['side'] == "Buy" and order['reduce_only'] == True
        buy_order_size = order['qty']  
        buy_order_id = order['order_id']

def get_sell_order():
    orders = client.get_active_order(symbol=symbol, limit=21)

    for order in orders['result']['data']:
        global sell_order
        global sell_order_id
        global sell_order_size
        sell_order = order['order_status'] == 'New' and order['side'] == "Sell" and order['reduce_only'] == False
        sell_order_id = order['order_id']
        sell_order_size = order['qty']
 

while True:

    get_6ema()
    
    get_position()
    get_buy_order()
    get_sell_order()
    getOrderBook()

    min_tp_distance = round(sell_position_prce - ((ema6hgh - ema6low)/2),decimals)
    tp_distance = round(ema6hgh - (ema6hgh - ema6low),decimals)
    entry = round(ema6hgh + (ema6hgh - ema6low),decimals)

    # TP 
        
    if tp_order == False and sell_position_size != 0 and bid > min_tp_distance:
        try:
            place_active_order = client.place_active_order(
            side="Buy",symbol=symbol,order_type="Limit",
            price=min_tp_distance,
            qty=sell_position_size,
            time_in_force="GoodTillCancel",reduce_only=True,close_on_trigger=True)
        except:
            pass
    else:
        pass

    if tp_order == False and sell_position_size != 0 and bid < min_tp_distance:
        try:
            place_active_order = client.place_active_order(
            side="Buy",symbol=symbol,order_type="Market",
            qty=sell_position_size)
        except:
            pass
    else:
        pass
        
    if tp_order == True and sell_position_size > buy_order_size:
        try:               
            cancel_active_order = client.cancel_active_order(order_id=buy_order_id)
        except:
            pass
        try:               
            place_active_order = client.place_active_order(
                side="Buy",symbol=symbol,order_type="Limit",
                price=min_tp_distance,
                qty=sell_position_size,
                time_in_force="GoodTillCancel",reduce_only=True,close_on_trigger=True)
        except:
            pass
    else:
        pass

    # Entry

    if sell_position_size == 0:
        try:               
            cancel_active_order = client.cancel_active_order(order_id=sell_order_id)
        except:
            pass
    
    if ask > ema6hgh and sell_position_size == 0:
        try:               
            place_active_order = client.place_active_order(
                side="Sell",symbol=symbol,order_type="Limit",
                price=ask,
                qty=qty1,
                time_in_force="GoodTillCancel",reduce_only=False,close_on_trigger=False)
        except:
            pass

    # Entry 2

    if sell_position_size >= qty1:
        try:                          
            cancel_active_order = client.cancel_active_order(order_id=sell_order_id)
        except:
            pass
    
    if sell_position_size >= qty1 and ema6low > sell_position_prce and ask > ema6hgh and sell_position_size < maxq:
        try:               
            place_active_order = client.place_active_order(
                side="Sell",symbol=symbol,order_type="Limit",
                price=ask,
                qty=sell_position_size,
                time_in_force="GoodTillCancel",reduce_only=False,close_on_trigger=False)
        except:
            pass

    if ask > ema6hgh:
        print('Ask > EMA 6 High') 
    if ema6low > sell_position_prce and sell_position_prce != 0:
        print('EMA 6 Low > Enty Price, Ready to Average!!!')

    print(sell_position_prce, ema6low)

    time.sleep(3)