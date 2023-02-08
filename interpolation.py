import pandas as pd
import os
import plotly.graph_objects as go
import numpy as np
from collections import Counter
from scipy import interpolate

"""Загрузка таблицы"""

file = (os.path.abspath('calculation results/BPLA, series 1.csv')).replace('\\', '/')
df = pd.read_csv(file, sep = ',', skiprows=3)
df.rename({'P1': 'a, град','P2': 'n, об/мин','P6': 'mx, Н*м','P7': 'fx, Н',}, axis=1, inplace=True) 
df = pd.DataFrame(df.iloc[:,1:])
df['n, об/мин'] *=-1
#______________________________________________________________________________________________________

"""Количество значений после расчётов"""

a_step = 2.5
n_step = 2000

a_counter_0 = round((df['a, град'].max() - df['a, град'].min())/a_step + 1)
n_counter_0 = round((df['n, об/мин'].max() - df['n, об/мин'].min())/n_step + 1)

"""Шаги интерполяции"""

inter = 5

a_step_inter = a_step/inter
n_step_inter = n_step/inter

print(a_step_inter, n_step_inter)