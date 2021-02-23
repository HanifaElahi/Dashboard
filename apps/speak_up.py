import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from app import app
from app import server

df1 = pd.read_csv("datasets/SpeakUp.csv")
months = df1['Month.1'] #taking the month column from dataframe
address = df1['Address.1'] #taking the address column from dataframe
stability = df1['Stability'] #taking the stability column from dataframe
cost_of_living = df1['Cost of Living'] #taking the cost of living column from dataframe
confidence = df1['Confidence'] #taking the confidence column from dataframe
happiness = df1['Happiness'] #taking the happiness column from dataframe

#creating dictionary
dict = {
    'Month' : months,
    'Address' : address,
    'Stability' : stability,
    'Cost of Living' : cost_of_living,
    'Confidence' : confidence,
    'Happiness' : happiness
}
df2 = pd.DataFrame(dict) 
#print(df2)

df = df2.groupby(['Month','Address'],sort = False)[['Stability','Cost of Living','Confidence','Happiness']].mean()
df.reset_index(inplace = True)


layout = html.Div([

    html.Br(),
    html.Br(),
    html.Br(),

    html.P('Stability,Cost of Living,Confidence,Happiness over a period of year on the basis of selected location', style={"textAlign": "center","color":"purple"}),

    html.Br(),

    html.Div([
    
        html.Div([
            html.Pre(children="Location", style={"fontSize": "150%","color":"purple","font-weight":"bold"}),
            dcc.Dropdown(
                id='location-dropdown', value='Kuwait, AlAhmadi', 
                options=[{'label': x, 'value': x} for x in sorted(df["Address"].unique())],
                style = {'color':'purple'},
            )
            ], className='six columns',style={"width": "100%"}),
    ], className='row'),

    dcc.Graph(id='my-map', figure={}),

    dash_table.DataTable(

            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            style_as_list_view=True,
            style_cell={'textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'purple',
                'fontWeight': 'bold',
                'color':'white'
    },

            data=df.to_dict('records'),
        ),


])

@app.callback(
    Output('my-map','figure'),
    [Input('location-dropdown', 'value')]
)

def display_value(location_chosen):
    df_fltrd = df[(df['Address'] == location_chosen)]
    df_fltrd = df_fltrd.groupby("Month",sort =False)[['Stability','Cost of Living','Confidence','Happiness']].mean()
    fig = px.line(df_fltrd)
    return fig



