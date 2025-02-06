# Bybit Scalp Bot 

Simple scalp bot for Bybit USDT Perpetual futures written on python

![image](https://user-images.githubusercontent.com/81808867/166137110-5b729e9a-88a6-409e-8891-9e6fb205bd17.png)


This simple bot written with python.If ask > EMA 6 high and Stoch > 80 it enters the market using limit orders and immediately place limit close order. In this example it will trade on XRPUSDT pair, but you can change it in settings. Please keep in mind that this example bot will <u>open only short</u> trades.

## How to use
- Edit config.py file, add you API credentials and change initial lot size.
- Run python3 xrp.py

## Entry logic
Bot will check EMA 6 High and if price higher it will start placing entry sell orders. It will add x2 size if EMA6 Low > Entry Price.
This bot will execute only short trades

## Requirements
Run pip install to install:

<code>pip install ta</code>

<code>pip install ccxt</code>

<code>pip install pandas</code>

<code>pip install pybit==2.4.1</code>

## Known issue
First you have to place sell order manually and delete it. Or leave it bot will delete it. Or it will send errors about entry size.

## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

🐀 Join Bybit and receive up to $6,045 in Bonuses: https://www.bybit.com/invite?ref=X2PZB

😎 Register on BingX and get a **20% discount** on fees: https://bingx.com/invite/HAJ8YQQAG/


## VPS for bots and scripts
I prefer using DigitalOcean. 
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
