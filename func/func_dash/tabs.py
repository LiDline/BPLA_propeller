import dash_bootstrap_components as dbc
from dash import html, dcc


from func.graph_2d import graph_2d
from func.func_dash.dropdown import dropdown_for_3d_graphs, dropdown_for_2d_graphs
# from func.cross_points_f import cross_points_f
# from func.cross_points_mx_w import cross_points_mx_w

def tabs():
    dropdown1 = dropdown_for_3d_graphs()
    dropdown2 = dropdown_for_2d_graphs()

    tab1_content = dbc.Card(
        dbc.CardBody([
                dbc.Row([
                dbc.Col(html.Div('Выбор данных:'))
            ]),
            dbc.Row([
                dbc.Col([dropdown1], width={"size": 2}, style={'margin-top': '10px'})
            ]),
            # 3D graphs
            dbc.Row([
                dbc.Col([html.Div(id='3d_plot')], md=6),
                ]),
            ]),
        className="mt-3",)

    tab2_content = dbc.Card(
        dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.P("График зависимости тяги от потребляемой мощности", className="card-text"))
                ]),
                dbc.Row([
                    dbc.Col([dcc.Graph(figure=graph_2d())], width={"size": 9, "offset": 0}),
                    dbc.Col([dropdown2], width={"size": 2})
                ]),
                dbc.Row([dbc.Col([
                    dbc.Alert("Видим, что существуют точки, тяга которых падает с увеличением мощности."),
                                ], width={"size": 4})
                        ]),
            ]),
        className="mt-3",)
    
    tab3_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Винт состоит из двух лопастей. Каждая лопасть представляет профиль крыла 20 х 4 мм и длинною 150 мм.", className="card-text"),
                # html.P("На рисунке представлена схема винта.", className="card-text"),
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