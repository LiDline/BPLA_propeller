import plotly.graph_objects as go   


from func.prepare_data import prepare_data


# 2D график Fx от W
def graph_2d():
    mx, fx, w, p, mx_m, fx_m, w_m, p_m, df, n_number, a_number = prepare_data()
    fig = go.Figure()

    fig.add_trace(go.Scatter(x = fx, 
                             y = w, mode = 'markers', 
                             line=dict(color='royalblue', width=0.5)))

    fig.update_xaxes(title_text="Fx, Н")
    fig.update_yaxes(title_text="Wв, Вт")

    fig.update_layout(
        # autosize=False, width=900, height=600,
        margin=dict(l=80, r=100,b=50,t=50,pad=4)
        )
    return fig