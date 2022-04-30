# Bybit Scalp Bot
Simple scalp bot for Bybit USDT Perpetual futures written on python

This simple bot written with python and it enters the market using limit orders and immediately place limit close order. In this example it will trade on XRPUSDT pair, but you can change it in settings. Please keep in mind that this example bot will <u>open only short</u> trades.


<br>
<strong>How to use</strong>

- Edit config.py file, add you API credentials and change initial lot size.
- Run python3 xrp.py

<br>
<strong>Entry logic</strong>

Bot will check EMA 6 Highand if price higher it will start placing entry sell orders. It will add x2 size if EMA6 Low > Entry Price.

This bot will execute only short trades

<br>
<strong>Requirements</strong>

Run pip install to install:
- ta
- time
- ccxt
- pandas
- pybit


<br>
To start trading on Bybit please register here: https://www.bybit.com/en-US/invite?ref=P11NJW


<br><br>
<strong>Disclaimer</strong>
<hr>
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
<hr>

<br>
<strong>Contacts</strong>

Feel free to contact me via Discord: ryuryu#4087
or join Discord group here: https://discord.gg/zSw58e9Uvf

