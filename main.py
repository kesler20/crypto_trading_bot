# Importing the API and instantiating the REST client according to our keys
import alpaca_trade_api as api
from config import *

BASE_URL = "https://paper-api.alpaca.markets"

alpaca = api.REST(API_KEY, SECRET_KEY, BASE_URL)
account = alpaca.get_account()
print(account)
# Setting parameters for the buy order
symbol = "BTC/USD"
qty = 0.01
# Submitting a market buy order by quantity of units to buy
order = alpaca.submit_order(symbol, qty=qty)
print(order)
# Get all open positions and print each of them
positions = alpaca.list_positions()
for position in positions:
    print(position)