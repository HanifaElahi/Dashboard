import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pathlib
from app import app
from app import server

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("speak_up.csv"))

data_list = ["Stability", "Cost of Living", "Confidence", "Happiness"]


layout = html.Div(children=[


        html.Br(),
        html.Br(),
        html.Br(),

        

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["Area"],
                        "y": df["Rate"],
                        "type": "bar",
                        
                        'marker': {
                                'color': 'purple'
                                 }
                    },
                ],
                 
                "layout": {"title": "Mappings","paper_bgcolor" : "lightgrey","plot_bgcolor":"lightgrey"},
            },
            
        ),
        

        html.Br(),
        html.Br(),
        html.Br(),

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
    ],
)


    
    