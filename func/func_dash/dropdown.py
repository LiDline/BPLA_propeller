from dash import dcc


# Меню выбора графика
def dropdown_for_3d_graphs():
    names = ["Fx, Н", "Mx, Н*м", "Wв, Вт", "P, Н/Вт"]
    options = []
    for key in names:
        options.append({'label': key, 'value' : key})

    return dcc.Dropdown(id='dropdown1', 
                                options = options,
                                value = "Fx, Н",
                                )

def dropdown_for_2d_graphs():
    names = ["Все точки", "Множество Парето"]
    options = []
    for key in names:
        options.append({'label': key, 'value' : key})
        
    return dcc.Dropdown(id='dropdown2', 
                                options = options,
                                value = "Все точки",
                                )