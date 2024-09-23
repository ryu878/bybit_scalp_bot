# Bybit Scalp Bot <a href="https://github.com/ryu878/bybit_scalp_bot/blob/main/LICENSE.MD">![image](https://camo.githubusercontent.com/83d3746e5881c1867665223424263d8e604df233d0a11aae0813e0414d433943/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)</a>
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

To start trading on Bybit please register here: https://www.bybit.com/en-US/invite?ref=P11NJW


## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch

Join me at Bybit and earn exclusive rewards with Bybit's Referral Program! 
Up to 1,025 USDT in rewards await you. https://www.bybit.com/invite?ref=P11NJW

## VPS for bots and scripts
I prefer using DigitalOcean. 
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
