import pandas as pd
import os
import numpy as np
import scipy.interpolate as spi

"""Загрузка таблицы"""

file = (os.path.abspath('calculation results/BPLA, series 1.csv')).replace('\\', '/')

df = pd.read_csv(file, sep = ',', skiprows=3)
df.rename({'P7': 'a, град','P8': 'n, об/мин','P3': 'fx, Н','P4': 'mx, Н*м',}, axis=1, inplace=True) 
df = pd.DataFrame(df.iloc[:,1:])
df['n, об/мин'] *=-1
df['a, град'] *=-1
#______________________________________________________________________________________________________

"""Количество значений после расчётов"""

a_step = 2.5
n_step = 2000

a_counter_0 = round((df['a, град'].max() - df['a, град'].min())/a_step + 1)
n_counter_0 = round((df['n, об/мин'].max() - df['n, об/мин'].min())/n_step + 1)
# print(a_counter_0)

"""Шаги интерполяции"""

a_step_inter = 1
n_step_inter = 1000

"""Интерполяция по n"""

name = ['mx, Н*м', 'fx, Н']
n = np.array(df.loc[:n_counter_0-1, 'n, об/мин'].values)
fx = np.array(df.loc[:, 'fx, Н'].values)
# print(fx)

counter_after_inter_n = a_counter_0 * len(np.arange(int(df['n, об/мин'].min()), int(df['n, об/мин'].max())+n_step_inter, n_step_inter))

i = 0
parametr = []
list1 = []

for l in range (0, len(name)):
    for j in range (0, (len(fx)//n_counter_0)):
        R1 = np.array(df.loc[i:i+n_counter_0-1, name[l]].values)
        f = spi.interp1d(n, R1, kind = 'cubic')
        list1 = f(np.arange(int(df['n, об/мин'].min()), int(df['n, об/мин'].max())+n_step_inter, n_step_inter))
        parametr = np.append(parametr, list1)
        i += n_counter_0
    i = 0

mx_inter_n = parametr[name.index('mx, Н*м')*counter_after_inter_n : name.index('mx, Н*м')*counter_after_inter_n + counter_after_inter_n]
fx_inter_n = parametr[name.index('fx, Н')*counter_after_inter_n : name.index('fx, Н')*counter_after_inter_n + counter_after_inter_n]
# print(fx_inter_n)

"""Интерполяция по a"""

a = np.arange(df['a, град'].min(), df['a, град'].max()+a_step, a_step)

# записал новые значения в виде матрицы, где каждая строка - это h2
k = 0
mx_matrix = np.zeros((len(mx_inter_n)//len(list1), len(list1)))
fx_matrix = np.zeros((len(mx_inter_n)//len(list1), len(list1)))

for i in range (0, len(mx_inter_n)//len(list1)):
    for j in range (0, len(list1)):
        mx_matrix[i,j] = mx_inter_n[k]
        fx_matrix[i,j] = fx_inter_n[k]
        k += 1

R1 = np.array(mx_matrix[:,:1])

mx_inter_matrix = np.zeros((len(R1)//a_counter_0 *  #количество диапазонов a
                           len(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter)), len(list1)))
fx_inter_matrix = np.zeros((len(R1)//a_counter_0 *  #количество диапазонов a
                           len(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter)), len(list1)))

def inter_a (matrix1, matrix2):
    R2 = []
    R3 = []

    for i in range (0, len(list1)):
        R1 = np.array(matrix1[:,i:i+1])
        R4 = []
        for j in range (0, len(R1), a_counter_0):
            R2 = R1[j:j+a_counter_0].transpose()
            f = spi.interp1d(a, R2, kind = 'cubic') # fill_value="extrapolate",
            R3 = f(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter))
            R4 = np.array(np.append(R4, R3))
            R5 = np.zeros((len(R4),1)) 
            for k in range(0, len(R4)):
                R5[k] = R4 [k]
        matrix2[:, i:i+1] = R5
    return matrix2
    
mx_matrix = inter_a(mx_matrix, mx_inter_matrix)
fx_matrix = inter_a(fx_matrix, fx_inter_matrix)

# записал новые значения в виде строки для таблицы
k = 0
mx_str = np.zeros(len(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter))*
                              len(mx_inter_matrix[:1,:].transpose()))
fx_str = np.zeros(len(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter))*
                              len(mx_inter_matrix[:1,:].transpose()))

for i in range (0, len(np.arange(df['a, град'].min(), df['a, град'].max()+a_step_inter, a_step_inter))):
    for j in range (0, len(mx_inter_matrix[:1,:].transpose())):
        mx_str[k] = mx_matrix[i,j]
        fx_str[k] = fx_matrix[i,j]
        k += 1

"""Заполнение таблицы"""

n_str = []
list2 = []

for i in range (0, len(mx_str)//len(list1)):
    n_str = np.append(n_str, np.arange(int(df['n, об/мин'].min()),int(df['n, об/мин'].max())+n_step_inter, n_step_inter))
# print(len(n_str))

a_str = []
list2 = []

k = df['a, град'].min()
for i in range (0, len(mx_str)//len(list1)):
    list2 = [k] * len(mx_matrix[0])
    a_str =  np.append(a_str, list2)
    k += a_step_inter
# print(len(a_str), a_str)

df_inter = pd.DataFrame(columns = ['a, град','n, об/мин','Fx, Н','Mx, Н*м',])

df_inter['a, град'] = a_str
df_inter['n, об/мин'] = n_str
df_inter['Mx, Н*м'] = mx_str
df_inter['Fx, Н'] = fx_str
df_inter["Wв, Вт"] = df_inter['n, об/мин']*df_inter['Mx, Н*м']*np.pi/30
df_inter['P, Н/Вт'] = df_inter['Fx, Н'] / df_inter['Wв, Вт']
# df_inter['P, Н/Вт'].replace(np.nan, 0, inplace=True)

df_inter.to_csv('calculation results/BPLA, series 1 - инт.csv')