from yahoo_fin.stock_info import * 
import matplotlib.pyplot as plt 
import pandas as pd
import time

data: list = []
WAIT_TIME = 2 #seconds

def calculate_sma(df: pd.DataFrame, i: int):
    df[f'SMA{i}'] = df[0].rolling(i).mean()
    return df

while True:
    data.append(get_live_price('TSLA'))
    time.sleep(WAIT_TIME)
    print(data)
    df = pd.DataFrame(data)
    print(calculate_sma(df,5))