from distutils.log import debug
from tarfile import PAX_FIELDS
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

df = pd.read_csv('materiais.csv')
df = df.sort_values(by='Grupo')

fig = px.bar(df, x='Grupo', y='Classe', color='PDM', barmode='group')

app.layout = html.Div(children=[
    html.H1(children='Olá Dashboard'),

    html.Div(children='''
        Dash: A web application framework for you data.    
    '''),

    dcc.Graph(
        id='exemplo de gráfico',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)