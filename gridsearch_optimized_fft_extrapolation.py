import pandas as pd
import numpy as np
import pylab as pl
from numpy import fft
import random
import time
import collections
import itertools
from statistics import mean, median, stdev
from sklearn.metrics import mean_squared_error
import matplotlib.animation as animation
from collections import deque
import matplotlib.pyplot as plt
from itertools import count

main_df = pd.read_csv("BTCUSDT_1m.csv")
main_df['SMA_30'] = main_df.close.rolling(window=30).mean()
main_df = main_df[['close','SMA_30']]

def train(df,LENGTH_INPUT_ARRAY,FUTURE_PERIOD_PREDICT):
    
    def fourierExtrapolation1(x, n_predict):
        n = x.size
        n_harm = 10
        t = np.arange(0, n)
        p = np.polyfit(t, x, 1)
        x_notrend = x - p[0] * t
        x_freqdom = fft.fft(x_notrend)
        f = fft.fftfreq(n)
        indexes = list(range(n))
        indexes.sort(key = lambda i: np.absolute(f[i]))

        t = np.arange(0, n + n_predict)
        restored_sig = np.zeros(t.size)
        for i in indexes[:1 + n_harm * 2]:
            ampli = np.absolute(x_freqdom[i]) / n
            phase = np.angle(x_freqdom[i])
            restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
        return restored_sig + p[0] * t

    df['future'] = df['SMA_30'].shift(-FUTURE_PERIOD_PREDICT)
    df.dropna(inplace = True)
    fft_input_list = list(df.iloc[-LENGTH_INPUT_ARRAY:].SMA_30)
    training_list = list(df.iloc[-FUTURE_PERIOD_PREDICT:].future)
    x = np.array(fft_input_list)
    extrapolation = fourierExtrapolation1(x, FUTURE_PERIOD_PREDICT)
    validation_list = list(extrapolation)[-FUTURE_PERIOD_PREDICT:]
    mse = mean_squared_error(training_list, validation_list)
    
    return mse, fft_input_list, training_list, validation_list, list(extrapolation)

def predict(df,LENGTH_INPUT_ARRAY,FUTURE_PERIOD_PREDICT):
    
    def fourierExtrapolation1(x, n_predict):
        n = x.size
        n_harm = 10
        t = np.arange(0, n)
        p = np.polyfit(t, x, 1)
        x_notrend = x - p[0] * t
        x_freqdom = fft.fft(x_notrend)
        f = fft.fftfreq(n)
        indexes = list(range(n))
        indexes.sort(key = lambda i: np.absolute(f[i]))

        t = np.arange(0, n + n_predict)
        restored_sig = np.zeros(t.size)
        for i in indexes[:1 + n_harm * 2]:
            ampli = np.absolute(x_freqdom[i]) / n
            phase = np.angle(x_freqdom[i])
            restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
        return restored_sig + p[0] * t

    fft_input_list = list(df.iloc[-LENGTH_INPUT_ARRAY:].SMA_30)
    x = np.array(fft_input_list)
    extrapolation = fourierExtrapolation1(x, FUTURE_PERIOD_PREDICT)
    
    return fft_input_list, list(extrapolation)

SMA, close, x = deque(maxlen=100), deque(maxlen=100), deque(maxlen=100)
index = count()
colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41' # matrix green
]
plt.style.use("dark_background")
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light greyfor param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark greycolors = [
fig, ax = plt.subplots()

def animate(i):

    x_val = next(index)

    x.append(x_val)
    SMA.append(main_df.iloc[x_val]['SMA_30'])
    close.append(main_df.iloc[x_val]['close'])

    if main_df.iloc[x_val]['SMA_30'] != np.nan and len(SMA) == 100:

        #Train
        best_score = float("inf"); best_config = None; best_rtn = None;
        for a in range(2, 42, 2):
            for b in range(2, 20, 2):
                df = pd.DataFrame({'close':close,'SMA_30':SMA})
                config = [a,b]
                rtn = train(df,a,b)
                mse = rtn[0]
                if mse < best_score:
                    best_config, best_score, best_rtn = config, mse, rtn
                del df
        #Predict
        df = pd.DataFrame({'close':close,'SMA_30':SMA})
        prediction_rtn = predict(df,best_config[0],best_config[1])

        ax.cla()
        ax.grid(color='#2A3459')
        ax.scatter(range(len(x)),SMA,marker='o',color=colors[0],alpha=0.9)
        ax.plot(range(len(x),len(x)+best_config[1]),prediction_rtn[1][-best_config[1]:],color=colors[1])
        [t.set_color("#FFFFFF") for t in ax.xaxis.get_ticklabels()]
        [t.set_color("#FFFFFF") for t in ax.yaxis.get_ticklabels()]
        leg = ax.legend(['Trained FFT Prediction','Time Series 30 Min SMA'],fontsize=15)
        ax.set_xlabel('30 Minute Periods',color="FFFFFF",fontsize=15)
        ax.set_ylabel('30 Period SMA of Time Series',color="#FFFFFF",fontsize=15)
        ax.xaxis.label.set_color('#FFFFFF')
        ax.yaxis.label.set_color('#FFFFFF')
        for text in leg.get_texts():
            text.set_color("#FFFFFF")
        n_shades = 10
        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades
        for n in range(1, n_shades+1):    
            ax.scatter(range(len(x)),SMA,marker='o',linewidth=2+(diff_linewidth*n),alpha=alpha_value,color=colors[0])
            ax.plot(range(len(x),len(x)+best_config[1]),prediction_rtn[1][-best_config[1]:],linewidth=2+(diff_linewidth*n),alpha=alpha_value,color=colors[1])
        # plt.savefig(f'output/{x_val}.png')

ani = animation.FuncAnimation(plt.gcf(),animate,interval=100)
plt.show()