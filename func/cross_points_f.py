import numpy as np


# Фун-я нахождения точки пересечения двух отрезков по координатам
def cross_points_f(f, a_number, n_number, fx_m, df):
    x3 = 0
    x4 = 1
    y3 = f
    y4 = f

    x1 = np.zeros(a_number)
    x2 = np.zeros(a_number)
    y1 = np.zeros(a_number)
    y2 = np.zeros(a_number)

    x = range(0, round(max(df['n, об/мин']))+1000, 1000)

    for i in range (a_number):
        for k in range (n_number-1):
            if (fx_m[i, k] <= f) and (fx_m[i, k+1] >= f): 
                x1[i] = x[k]
                x2[i] = x[k+1]
                y1[i] = fx_m[i, k]
                y2[i] = fx_m[i, k+1]

    x = (((x1*y2-y1*x2)*(x3-x4)-(x1 - x2)*(x3*x4-y3*x4))/
                ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))
    
    return x