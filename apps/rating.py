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




df1 = pd.read_csv("datasets/rating.csv")

months = df1['Month']

entity = df1['X Entity']

division_1 = df1['X1 Division']

division_1_department_1 = df1['X11 Department']
division_1_department_1_agent = df1['X111 Agent']
division_1_department_1_service = df1['X112 Service']
division_1_department_1_location = df1['X113 Location']
division_1_department_1_callcenter = df1['X114 Call Center']
division_1_department_1_onlineservices = df1['X115 Online Service']

division_1_department_2 = df1['X12 Department']
division_1_department_2_agent = df1['X121 Agent']
division_1_department_2_service = df1['X122 Service']
division_1_department_2_location = df1['X123 Location']
division_1_department_2_callcenter = df1['X124 Call Center']
division_1_department_2_onlineservices = df1['X125 Online Service']

division_2 = df1['X2 Division']

division_2_department_1 = df1['X21 Department']
division_2_department_1_agent = df1['X211 Agent']
division_2_department_1_service = df1['X212 Service']
division_2_department_1_location = df1['X213 Location']
division_2_department_1_callcenter = df1['X214 Call Center']
division_2_department_1_onlineservices = df1['X215 Online Service']

division_2_department_2 = df1['X22 Department']
division_2_department_2_agent = df1['X221 Agent']
division_2_department_2_service = df1['X222 Service']
division_2_department_2_location = df1['X223 Location']
division_2_department_2_callcenter = df1['X224 Call Center']
division_2_department_2_onlineservices = df1['X225 Online Service']

dict1 = {
    'Month' : months,
    
    'Entity' : entity,
    
    'Division X1' : division_1,
    
    'Department X11' : division_1_department_1,
    'X111 Agent': division_1_department_1_agent,
    'X112 Service': division_1_department_1_service,
    'X113 Location': division_1_department_1_location,
    'X114 Call Center': division_1_department_1_callcenter,
    'X115 Online Service': division_1_department_1_onlineservices,
    
    'Department X12' : division_1_department_2,
    'X121 Agent': division_1_department_2_agent,
    'X122 Service': division_1_department_2_service,
    'X123 Location': division_1_department_2_location,
    'X124 Call Center': division_1_department_2_callcenter,
    'X125 Online Service': division_1_department_2_onlineservices,
    
    'Division X2' : division_2,
    
    'Department X21' : division_2_department_1,
    'X211 Agent': division_2_department_1_agent,
    'X212 Service': division_2_department_1_service,
    'X213 Location': division_2_department_1_location,
    'X214 Call Center': division_2_department_1_callcenter,
    'X215 Online Service': division_2_department_1_onlineservices,
    
    'Department X22' : division_2_department_2,
    'X221 Agent': division_2_department_2_agent,
    'X222 Service': division_2_department_2_service,
    'X223 Location': division_2_department_2_location,
    'X224 Call Center': division_2_department_2_callcenter,
    'X225 Online Service': division_2_department_2_onlineservices
    
}

df2 = pd.DataFrame(dict1) 

a = df2.groupby(["Month"],sort = False)['Entity'].mean()
b = df2.groupby(["Month"],sort = False)['Division X1'].mean()
c = df2.groupby(["Month"],sort = False)['Department X11'].mean()
d = df2.groupby(["Month"],sort = False)['X111 Agent'].mean()
e = df2.groupby(["Month"],sort = False)['X112 Service'].mean()
f = df2.groupby(["Month"],sort = False)['X113 Location'].mean()
g = df2.groupby(["Month"],sort = False)['X114 Call Center'].mean()
h = df2.groupby(["Month"],sort = False)['X115 Online Service'].mean()
i = df2.groupby(["Month"],sort = False)['Department X12'].mean()
j = df2.groupby(["Month"],sort = False)['X121 Agent'].mean()
k = df2.groupby(["Month"],sort = False)['X122 Service'].mean()
l = df2.groupby(["Month"],sort = False)['X123 Location'].mean()
m = df2.groupby(["Month"],sort = False)['X124 Call Center'].mean()
n = df2.groupby(["Month"],sort = False)['X125 Online Service'].mean()
o = df2.groupby(["Month"],sort = False)['Division X2'].mean()
p = df2.groupby(["Month"],sort = False)['Department X21'].mean()
q = df2.groupby(["Month"],sort = False)['X211 Agent'].mean()
r = df2.groupby(["Month"],sort = False)['X212 Service'].mean()
s = df2.groupby(["Month"],sort = False)['X213 Location'].mean()
t = df2.groupby(["Month"],sort = False)['X214 Call Center'].mean()
u = df2.groupby(["Month"],sort = False)['X215 Online Service'].mean()
v = df2.groupby(["Month"],sort = False)['Department X22'].mean()
w = df2.groupby(["Month"],sort = False)['X221 Agent'].mean()
x = df2.groupby(["Month"],sort = False)['X222 Service'].mean()
y = df2.groupby(["Month"],sort = False)['X223 Location'].mean()
z = df2.groupby(["Month"],sort = False)['X224 Call Center'].mean()
aa = df2.groupby(["Month"],sort = False)['X225 Online Service'].mean()


dict2 = {
    'Entity' : a,
    'Division X1' : b,
    'Department X11' : c,
    'X111 Agent' : d,
    'X112 Service':e,
    'X113 Location':f,
    'X114 Call Center':g,
    'X115 Online Service':h,
    'Department X12':i,
    'X121 Agent':j,
    'X122 Service':k,
    'X123 Location':l,
    'X124 Call Center':m,
    'X125 Online Service':n,
    'Division X2':o,
    'Department X21':p,
    'X211 Agent':q,
    'X212 Service':r,
    'X213 Location':s,
    'X214 Call Center':t,
    'X215 Online Service':u,
    'Department X22':v,
    'X221 Agent':w,
    'X222 Service':x,
    'X223 Location':y,
    'X224 Call Center':z,
    'X225 Online Service':aa
}
df3 = pd.DataFrame(dict2)

all_categories = df3.columns.unique()

layout = html.Div([

    html.Br(),
    html.Br(),
    html.Br(),

    html.H1('Rating Analytics', style={"textAlign": "center","color":"purple"}),
    html.Br(),

    dcc.Dropdown(id='my_dropdown',
            options=[{'label': k, 'value': k} for k in dict2.keys()],
            optionHeight=35,                    
            value = "Entity", 
            disabled=False,                     
            multi=True,                        
            searchable=True,                    
            search_value='',                   
            placeholder='Select...',     
            clearable=True,                     
            style={'width':"100%",'color':'purple'},             
            
    ),  

    html.Br(),
                               

    html.Div([
        dcc.Graph(id='our_graph')
    ],className='twelve columns'),

    html.Br(),
    html.Br(),
    html.Br(),

    dash_table.DataTable(

            id='table',
            columns=[{"name": i, "id": i} for i in df3.columns],
            style_as_list_view=True,
            style_cell={'textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'purple',
                'fontWeight': 'bold',
                'color':'white'
    },

            data=df3.to_dict('records'),
        ),
])


@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)


def update_data(option):

    df_filterd = df3[option]
    fig = px.line(df_filterd)
    return fig
    
   