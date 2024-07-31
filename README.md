# How to Build a MetaTrader 5 Python Trading Bot (Expert Advisor) Series

This is the code for my series **How to Build a MetaTrader 5 Python Trading Bot** found on Medium @appnologyjames

The five part series covers all you need to get started building your very own Python Trading Bot. Each episode in the series contains working code samples to help you build your own.

## Join Our Community
We love connecting with our audience! Join us on the following links:
1. [Discord](https://discord.gg/wNYYGaMGfd)
2. [Telegram](https://t.me/TradeOxySupportBot)
3. [TradeOxy Platform](https://www.tradeoxy.com)
4. [Upcoming Content](https://tradeoxy.notion.site/Content-Creation-Roadmap-5f896060f39341fd9539bcaced8c3b5d)
5. [Upcoming Features](https://tradeoxy.notion.site/3f9666718dc24e38bbd4a56a741287ae?v=d810cfa006f54bafa4bbbe3674fefa98&pvs=74)
6. [Custom Trading Bot development](https://tradeoxy.notion.site/Trading-Bot-Pricing-Guide-f0ff11b0604b4b998cba2b8da6a129cb?pvs=4)

## Requirements
- Windows 10 or above endpoint (for whatever reason, MetaTrader doesn't support their Python API on macOS or Linux)
- MetaTrader 5 (note MetaTrader 4 doesn't have a Python API)
- A basic knowledge of Python, such as functions and variables
- Python 3 installed (my build version is 3.10)
- An IDE (I used [JetBrains Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/other.html))

## Medium Blog Series
### [Episode 1: Getting Started](https://appnologyjames.medium.com/metatrader5-python-trading-bot-230bd19285e9)
This episode covers everything you need to get started building your Python Trading Bot, including:
- How to set up your files
- How to securely import your settings, including username/password
- How to initialize your project through `___main___`
- Where to find the MetaTrader 5 Python API

### [Episode 2: Making Trades](https://appnologyjames.medium.com/how-to-build-a-metatrader-5-python-trading-bot-expert-advisor-making-trades-7188b5f78b23)
This episode shows you how to make and modify trades on MetaTrader 5. It covers:
- How to enable a trade symbol on MetaTrader 5
- Placing Trades
- Canceling an Order
- Modifying an open position

### [Episode 3: Automated Strategy](https://appnologyjames.medium.com/how-to-build-a-metatrader-5-python-trading-bot-expert-advisor-automated-strategy-dc2e32f1f902)
This episode demonstrates how to break down a strategy into a series of codified steps. By the end of the episode, you can take an untested strategy and implement it in your code. It covers:
- Setting up a program structure
- Design considerations
- Algorithmic decision making
- Initiating trades based on decisions
**Note: The algorithm used in this episode is simplistic and not recommended. It is for demonstration purposes only!**

### [Episode 4: Automated Trading](https://appnologyjames.medium.com/how-to-build-a-metatrader-5-python-trading-bot-expert-advisor-automated-trading-ab7ee10bf4a)
Demonstrates how to close the loop on your automated strategy, including:
- Design considerations for parallel processing, polling method for data
- Managing order queue
- Some further improvements to consider

### [Bonus Episode: Python Trailing Stop](https://appnologyjames.medium.com/metatrader-5-python-trailing-stop-2c562a541b48)
This episode shows you how to implement one of the most requested features I get: a trailing stop. It includes:
- An overview of a trailing stop
- Ways to take this code and improve it
- How to use the `modify_position()` function to trail a price
- How update an existing position

## YouTube Episodes
Our YouTube channel [TradeOxy](https://www.youtube.com/@tradeoxy) contains tons of helpful content on how
to use the AutoTrading Bot or build one for yourself. Check out these episodes:
1. [Secure Setup](https://www.youtube.com/watch?v=jpw3JltNMg0)
2. [Connect To MetaTrader 5 with Python](https://www.youtube.com/watch?v=EkP7iAZoMEw&t=2s)
3. [Retrieve 50000 Candlesticks from MetaTrader](https://www.youtube.com/watch?v=KZmVek6EDCg)
4. [Add the EMA Indicator to Your Algorithmic AutoTrading Bot](https://youtu.be/QqLjXecrKhc)
5. [How to Install TALib on Windows](https://youtu.be/jnxqu9MhBIE)
6. [Build Your Own AutoTrading Bot EMA Cross Detector](https://youtu.be/lbdO_UKEzQU)
7. [How to Trade the EMA Cross Strategy with Your AutoTrading Bot](https://youtu.be/A6RTl0_13pw)
8. [How to Convert Your AutoTrading Bot Strategy into BUY and SELL Signals](https://youtu.be/21NtSVuPaZw)
9. [How to Calculate Lot Size for Your MetaTrader 5 Python Trading Bot](https://youtu.be/fveyPFreenk)
10. [How to Create Orders with Your MetaTrader Python Trading Bot](https://youtu.be/fveyPFreenk)
