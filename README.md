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


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, liquidations, volume, delta, liquidity, spread behavior, funding)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL, ClickHouse
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
