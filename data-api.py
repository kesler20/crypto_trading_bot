from yahoo_fin.stock_info import * 
import matplotlib.pyplot as plt 
import pandas as pd
import time

data: list = []
WAIT_TIME = 2 #seconds

def calculate_sma(data: pd.DataFrame):
    col = data.columns
    result = []
    window = []
    window_size = 20
    for price in data[col[0]]:#
        window.append(price)
        if len(window) == window_size:
            result.append(sum(window)/window_size)
            del window
    return result

while True:
    data.append(get_live_price('TSLA'))
    time.sleep(WAIT_TIME)
    print(data)
    # print(data)
    # df = pd.DataFrame(data)
    # df.to_csv('data.csv')
    calculate_sma(data)