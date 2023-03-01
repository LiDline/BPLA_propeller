import dash_bootstrap_components as dbc
from dash import html, dcc


from func.graph_2d import graph_2d
# from func.cross_points_f import cross_points_f
# from func.cross_points_mx_w import cross_points_mx_w

def tabs():
    # Меню выбора графика
    names = ["Fx, Н", "Mx, Н*м", "Wв, Вт", "P, Н/Вт"]
    options = []
    for key in names:
        options.append({'label': key, 'value' : key})
        
    dropdown = dcc.Dropdown(id='dropdown1', 
                                options = options,
                                value = "Fx, Н",
                                )

    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                dbc.Row([
                dbc.Col(html.Div('Выбор данных:'))
            ]),
            dbc.Row([
                dbc.Col([dropdown], width={"size": 1}, style={'margin-top': '10px'})
            ]),
            # 3D graphs
            dbc.Row([
                dbc.Col([html.Div(id='3d_plot')], md=6),
                ]),
            ]),
        className="mt-3",)

    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col(html.P("График зависимости тяги от потребляемой мощности", className="card-text"))
                ]),
                dbc.Row([
                    dbc.Col([dcc.Graph(figure=graph_2d())], width={"size": 10, "offset": 0}),
                ])
            ]),
        className="mt-3",)
    
    tab3_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Здесь будет описание работы", className="card-text"),
            ]
        ),
        className="mt-3",
    )

    tabs = dbc.Tabs(
        [
            dbc.Tab(tab1_content, label="3D графики"),
            dbc.Tab(tab2_content, label="2D графики"),
            dbc.Tab(tab3_content, label="Описание"),
        ]
    )
    return tabs