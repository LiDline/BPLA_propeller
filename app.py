# from dash_extensions.enrich import html, dcc, Output, Input, DashProxy
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc


from func.prepare_data import prepare_data
from func.func_dash.tabs import tabs
from func.func_dash.data_for_dropdown_plot import data_for_dropdown_plot

'''Data for dropdown graphs'''
mx, fx, w, p, mx_m, fx_m, w_m, p_m, df, n_number, a_number = prepare_data()
di_for_dropdown_plot = data_for_dropdown_plot(mx, fx, w, p, mx_m, fx_m, w_m, p_m, df, n_number, a_number)

'''App'''

app = Dash(name="graphs", external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.H1('Двухлопастной винт (20 х 4 х 150 мм)', style={'textAlign': 'center','margin-top': '10px'})

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
    Output('3d_plot', 'children'),
    Input('dropdown1', 'value')
)
def choise_plot(key):
    try:
        plot = dcc.Graph(figure=di_for_dropdown_plot[key])
    except:
        plot = html.Div('Пожалуйста, выберите данные в поле выше', style={'margin-top': '10px'})
    return plot

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)