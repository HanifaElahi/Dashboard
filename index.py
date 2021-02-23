import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import rating, say_more, speak_up, visualization


colors = {
    'background':'white',
    'text':'purple'
}

#-----------------------------------------------------------------------------------------------------------------------
app.layout = html.Div([

    html.H1(
        children = 'Dashboard',
        style = {
            'textAlign':'center',
            'font-size':'450',
            'background':'white',
            'color':'purple',
            'inline-style':'box'
        }
    ),

       
    dcc.Location(id='url', refresh=True),
    html.Div([
    
        dcc.Link('Mappings', href='/apps/visualization',
        style={'background-color': 'purple','color':'white','padding':'1.25em 9.1em','text-decoration':'none','font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
        
        dcc.Link('Speak Up', href='/apps/speak_up',
        style={'background-color': 'purple','color':'white','padding':'1.25em 9.1em','text-decoration':'none','font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
        
        dcc.Link('Say More', href='/apps/say_more',
        style={'background-color': 'purple','color':'white','padding':'1.25em 9.1em','text-decoration':'none','font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
      
        dcc.Link('Rating', href='/apps/rating',
        style={'background-color': 'purple','color':'white','padding':'1.25em 9.1em','text-decoration':'none','font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),  
    
]),
        


    html.Div(id='page-content', children=[])
])

#------------------------------------------------------------------------------------------------------------------

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/visualization':
        return visualization.layout
    if pathname == '/apps/speak_up':
        return speak_up.layout
    if pathname == '/apps/say_more':
        return say_more.layout
    if pathname == '/apps/rating':
        return rating.layout



if __name__ == '__main__':
    app.run_server(debug=False)
    