from yahoo_fin.stock_info import * 
import matplotlib.pyplot as plt 
import pandas as pd
import time

data: list = []
WAIT_TIME = 2 #seconds
while True:
    data.append(get_live_price('TSLA'))
    time.sleep(WAIT_TIME)
    print(data)
    df = pd.DataFrame(data)
    df.plot()
    plt.show()