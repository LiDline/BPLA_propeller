import plotly.graph_objects as go


from func.graph_3d import graph_3d


# Запишем нужные данные
def data_for_dropdown_plot(mx, fx, w, p, mx_m, fx_m, w_m, p_m, df, n_number, a_number):

    Fx = graph_3d(go.Figure(), fx_m, fx, df, a_number, n_number, 'Fx, Н')
    Fx.basic_plot([[0,'rgb(255, 0, 0)'], [1, 'rgb(255, 0, 0)']])

    Mx = graph_3d(go.Figure(), mx_m, mx, df, a_number, n_number, 'Mx, Н*м')
    Mx.basic_plot([[0,'rgb(255, 165, 0)'], [1, 'rgb(255, 165, 0)']])

    W = graph_3d(go.Figure(), w_m, w, df, a_number, n_number, 'Wв, Вт')
    W.basic_plot([[0,'rgb(66, 170, 255)'], [1, 'rgb(66, 170, 255)']])

    P = graph_3d(go.Figure(), p_m, p, df, a_number, n_number, 'P, Н/Вт')
    P.basic_plot([[0,'rgb(144, 238, 144)'], [1, 'rgb(144, 238, 144)']])
    
    di = {'Fx, Н' : Fx.return_fig(), 'Mx, Н*м' : Mx.return_fig(), 'Wв, Вт' : W.return_fig(), 'P, Н/Вт' : P.return_fig()}
    
    return di