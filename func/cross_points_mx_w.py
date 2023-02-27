import numpy as np


# Фун-я нахождения точки пересечения двух отрезков по координатам
def cross_points_mx_w(n, a_number, n_number, matrix, df):
    x3 = n
    x4 = x3
    y3 = 0
    y4 = 10000

    x1 = np.zeros(a_number)
    x2 = np.zeros(a_number)
    y1 = np.zeros(a_number)
    y2 = np.zeros(a_number)

    x = range(0, round(max(df['n, об/мин']))+1000, 1000)

    for i in range (a_number):
        for k in range (n_number):
            if x[k] <= x3[i] and x[k+1] >= x3[i]: 
                x1[i] = x[k]
                x2[i] = x[k+1]
                y1[i] = matrix[i, k]
                y2[i] = matrix[i, k+1]

    y = (((x1*y2 - y1*x2) * (y3-y4) - (y1 - y2) * (x3*y4 - y3*x4))/
        ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 -x4)))   

    return y