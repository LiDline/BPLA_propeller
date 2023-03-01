import plotly.graph_objects as go
from datetime import date
import numpy as np

class graph:

    def __init__(self, fig, z_An_matrix, z_An_string, df, a_number, n_number, title_left):
        self.z_An_matrix = z_An_matrix
        self.z_An_string = z_An_string
        self.df = df
        self.a_number = a_number
        self.n_number = n_number
        self.title_left = title_left
        self.fig = fig

    def return_fig(self):
        return self.fig

    # Орисовка сетки на поверхности
    def mesh(self):
        opa_mesh = 0.4
        k = 0
        
        z1 = np.zeros((self.n_number))
        for i in range (0, self.a_number):
            for j in range(0, self.n_number):
                z1[j] = self.z_An_string[k]  
                k += 1                
            self.fig.add_trace(go.Scatter3d(x=list(range(0,int(self.df['n, об/мин'].max())+1000, 1000)), y=[i]*self.n_number, z=z1, 
                                    showlegend=False, legendgroup="group", opacity = opa_mesh,
                                   marker=dict(size=1,color='black',colorscale='Viridis',),
                                   line=dict(color='black', width=3)))

            self.fig.add_trace(go.Scatter3d(x=[int(self.df['n, об/мин'].max()) - i*1000]*self.a_number, y=list(range(0, self.a_number)),
                                             z=np.array(self.df.loc[(self.df.loc[:, 'n, об/мин']==int(self.df['n, об/мин'].max())-i*1000), 
                                                                    self.title_left]),
                                             showlegend=False, legendgroup="group", opacity = opa_mesh,
                                             marker=dict(size=1,color='black',colorscale='Viridis',),
                                             line=dict(color='black', width=3))) 
            

    # Отрисовка пов-сти
    def basic_plot(self, color): 

        opa_sur = 0.95

        x = list(range(int(self.df['n, об/мин'].min()), int(self.df['n, об/мин'].max())+1000,1000))
        y = list(range(0, self.a_number+1, 1))

        self.fig.add_trace(go.Surface(x=x, y=y, z = self.z_An_matrix, 
                        opacity=opa_sur, showscale=False, showlegend=True,
                        name = f'Поверхность {self.title_left}',
                        legendgroup="group", 
                        colorscale=color))

        #                                                             Сетка
        self.mesh()

    #_________________________________________________________________________________________________________________________   

                                                  #Оформление 
    
        tickf = 12
        self.fig.update_layout(autosize=False,
                      scene = {"aspectratio": {"x": 1, "y": 1, "z": 1},  #Масштаб осей
                      'camera_eye': {"x": -2, "y": 2, "z":1.65},
                    'camera_center' : {"x": 0, "y": 0, "z":0},},                
        )

        self.fig.update_layout(scene=dict(xaxis=dict(title="n, об/мин",
                            backgroundcolor="rgb(200, 200, 230)",
                             gridcolor="white",
                             showbackground=True,
                             zerolinecolor="white", tickfont=dict(size=tickf)),
        yaxis=dict(title="a, град", 
                            backgroundcolor="rgb(230, 200,230)",
                            gridcolor="white",
                            showbackground=True,tickfont=dict(size=tickf),
                            zerolinecolor="white"),
        zaxis=dict(title=self.title_left, backgroundcolor="rgb(200, 200,200)",
                             gridcolor="white",
                             showbackground=True,tickfont=dict(size=tickf),
                             zerolinecolor="white",)))
        self.fig.update_layout(scene=dict(xaxis_showspikes=False, yaxis_showspikes=False),) #Изменение при наведении мышки
        self.fig.update_scenes(camera_projection_type="orthographic") #вводит ортогональный вид

     #__________________________________________________________    
                                #Легенда

        self.fig.update_layout(showlegend=True)
        self.fig.update_layout(legend=dict(    #Изменение положения легенды
        yanchor="top",
        y=1,
        xanchor="left",
        x=0.6, 
        title_font_family="Times New Roman",
    #     bgcolor=None
        ))   

        self.fig.update_layout(
            autosize=False,width=800,height=700,
            margin=dict(l=50, r=50,b=50,t=50,pad=4))

        self.fig.update_layout(
            title=f"Лопасть 20 х 4 х 150 мм;  {date.today()}",
            # legend_title="Legend Title",
            )

        self.fig.update_layout(           #Позиционирование заголовка
            title={
               'text': f"Двухлопастной винт (20 х 4 х 150 мм); {date.today()}",
               'y':0.97,
               'x':0.5,
               'xanchor': 'center',
               'yanchor': 'top'})

        # self.fig.show()


    # Линия пересечения
    def cross_line(self, x, z, f, color='black', showlegend=True):
        self.fig.add_trace(go.Scatter3d(x=x, y=list(range(0, round(max(self.df['a, град']))+1, 1)), z=z, 
                                    showlegend=showlegend, name = f'Fx = {f} Н', legendgroup=f"group{f}", 
                                    opacity = 1, marker=dict(size=1,color='black',colorscale='Viridis',),
                                    line=dict(color=color, width=6)))


    def basic_line(self, x, y, f):
        self.cross_line(x, [0]*len(x), f, 'yellow', False)

        for i in range(0, len(x), 4):
             self.fig.add_trace(go.Scatter3d(x=[x[i], x[i]], y=[y[i], y[i]], 
                                   z=[35, 0], showlegend=False,
                                   legendgroup=f"group{f}",  opacity=1,
                                   marker=dict(size=1, color='royalblue', colorscale='Viridis',), 
                                   line=dict(color='black', width=6, dash='dash')))
        
    def annotation(self, x, y, f):
            
        self.fig.add_trace(go.Scatter3d(x=[x[30], x[30]], y=[y[30], y[30]], 
                                   z=[35, 0], showlegend=False,
                                   legendgroup=f"group{f}",  opacity=1,
                                   marker=dict(size=1, color='royalblue', colorscale='Viridis',), 
                                   line=dict(color='black', width=6)))
        self.fig.add_trace(go.Scatter3d(x=[x[30], 0], y=[y[30], y[30]], z=[0,0], 
                                        showlegend=False,
                                        legendgroup=f"group{f}",  opacity=1,
                                        marker=dict(size=3, color='royalblue', colorscale='Viridis',), 
                                        line=dict(color='royalblue', width=4)))
        self.fig.add_trace(go.Scatter3d(x=[x[30], x[30]], y=[y[30], 0], 
                                   z=[0, 0], showlegend=False,
                                   legendgroup=f"group{f}",  opacity=1,
                                   marker=dict(size=3, color='royalblue', colorscale='Viridis',), 
                                   line=dict(color='royalblue', width=4)))

            #Точка пересечения
        self.fig.update_layout(
            scene=dict(
            annotations=[dict(x=0, y=y[30], z=0,
                            text=f"{round(y[30])} [град]", textangle=0, ax=20, ay=-40,
                            bordercolor="#c7c7c7", borderwidth=2, borderpad=4, 
                            bgcolor="white", opacity=0.8,
                            font=dict(color="black", size=12),arrowcolor="black", arrowsize=1, 
                            arrowwidth=1, arrowhead=1),

                            dict(x=x[30], y=0, z=0,
                                text=f"{round(x[30])} [об/мин]", textangle=0, ax=-20, ay=-40,
                                bordercolor="#c7c7c7", borderwidth=2, borderpad=4,
                                bgcolor="White", opacity=0.8,
                                font=dict( color="black", size=12),
                                arrowcolor="black", arrowsize=1, arrowwidth=1, arrowhead=1),

                            dict(x=x[30], y=y[30], z=f, text="Линия пересечения", 
                                textangle=0, ax=-42, ay=-60, 
                                bordercolor="#c7c7c7", borderwidth=2, borderpad=4, 
                                bgcolor="white", opacity=0.8,
                                font=dict( color="black", size=12),
                                arrowcolor="black", arrowsize=1, arrowwidth=1, arrowhead=1),
                                ]))


    # Горизонтальная плоскость                                            
    def horizontal_cross_palne(self, f):
        opa_0_plane = 0.3

        self.fig.add_trace(go.Scatter3d(x=[0, self.df['n, об/мин'].max(), self.df['n, об/мин'].max(), 0, 0],
                                       y=[0, 0, self.df['a, град'].max(), self.df['a, град'].max(), 0],
                                       z=[f, f, f, f, f], showlegend=False,
                                       surfaceaxis=2, 
                                       opacity=opa_0_plane, legendgroup=f"group{f}",
                                       marker=dict(size=1, color='white', colorscale='Viridis',)))
        self.fig.add_trace(go.Scatter3d(x=[0, self.df['n, об/мин'].max(), self.df['n, об/мин'].max(), 0, 0],
                                       y=[0, 0, self.df['a, град'].max(), self.df['a, град'].max(), 0],
                                       z=[f, f, f, f, f], showlegend=False,
                                       surfaceaxis=-1, 
                                       opacity=1, legendgroup=f"group{f}",
                                       marker=dict(size=2, color='black')))