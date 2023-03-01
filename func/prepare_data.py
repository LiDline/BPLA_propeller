import os
import pandas as pd
from collections import Counter
import numpy as np


# Подготовим данные для графиков
def prepare_data():
    file = (os.path.abspath('calculation results/BPLA, series 1 - инт.csv')).replace('\\', '/')
    df = pd.read_csv(file, sep = ',')
    df = pd.DataFrame(df.iloc[:,1:])
    
    mx = np.array(df.loc[:, 'Mx, Н*м'].values)
    fx = np.array(df.loc[:, 'Fx, Н'].values)
    w = np.array(df.loc[:, 'Wв, Вт'].values)
    p = np.array(df.loc[:, 'P, Н/Вт'].values)
    
    
    for number, n_number in Counter(df['a, град']).items():
        break
    for number, a_number in Counter(df['n, об/мин']).items():
        break
    
    # Подготовим матрицы для графиков
    k = 0
    
    mx_m, fx_m, w_m, p_m = np.zeros((a_number, n_number)), np.zeros((a_number, n_number)), np.zeros((a_number, n_number)), np.zeros((a_number, n_number))
    for i in range (0, a_number):
        for j in range (0, n_number):
            mx_m[i,j], fx_m[i,j], w_m[i,j], p_m[i,j] = mx[k], fx[k], w[k], p[k]
            k += 1 
            
    return mx, fx, w, p, mx_m, fx_m, w_m, p_m, df, n_number, a_number