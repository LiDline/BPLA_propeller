# from dash_extensions.enrich import html, dcc, Output, Input, DashProxy
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc


from func.tabs import tabs
from func.data_for_plot import data_for_plot

'''Data for graphs'''

di = data_for_plot()

'''App'''

app = Dash(name="graphs", external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.H1('BPLA', style={'textAlign': 'center','margin-top': '10px'})

'''layout'''

app.layout = html.Div([
    # header
    dbc.Row([
            dbc.Col([header])
    ]),
    dbc.Row([tabs()
    ])
], style={'margin-left': '80px', 'margin-right': '80px'})

'''callback'''

@app.callback(
    Output('plot', 'children'),
    Input('dropdown1', 'value')
)
def choise_plot(key):
    try:
        plot = dcc.Graph(figure=di[key])
    except:
        plot = html.Div('Пожалуйста, выберете данные', style={'margin-top': '10px'})
    return plot

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)