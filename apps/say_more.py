import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import numpy as np
import re
import string
import spacy
import nltk
from dash.dependencies import Input, Output
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
nlp = spacy.load("en_core_web_sm")
from app import app
from app import server

df1 = pd.read_csv("datasets/SayMore.csv")

complain = df1['Complain'] #taking the complain column from dataframe
suggestion = df1['Suggestion'] #taking the suggestion column from dataframe
feedback = df1['FeedBack'] 

#creating dictionary
dict = {
    'Complain' : complain,
    'Suggestion' : suggestion,
    'Feedback' : feedback
}

df2 = pd.DataFrame(dict)
df2['Complain'] = df2['Complain'].str.lower()
df2['Feedback'] = df2['Feedback'].str.lower()
df2['Suggestion'] = df2['Suggestion'].str.lower()

df2['Suggestion'] = df2['Suggestion'].str.replace("[^a-zA-Z]"," ")
df2['Complain'] = df2['Complain'].str.replace("[^a-zA-Z]"," ")
df2['Feedback'] = df2['Feedback'].str.replace("[^a-zA-Z]"," ")

stop_words = stopwords.words('english') #stopwords from nltk
all_stopwords = nlp.Defaults.stop_words #stopwords from nlp
#function for removing stopwords
def stopwords(data):
    text = [word.lower() for word in data.split() if word.lower() not in stop_words and word.lower() not in all_stopwords]
    return " ".join(text)

#applying stopwords removal function
df2['Complain'] = df2['Complain'].apply(stopwords)
df2['Feedback'] = df2['Feedback'].apply(stopwords)
df2['Suggestion'] = df2['Suggestion'].apply(stopwords)


#initializing lemmatizer
lem = WordNetLemmatizer()
#function for lemmatization
def lemmatize(resume):
    lem_text = [lem.lemmatize(word) for word in resume.split()]
    return " ".join(lem_text)

#applyinh lemmatization
df2['Complain'] = df2['Complain'].apply(lemmatize)
df2['Feedback'] = df2['Feedback'].apply(lemmatize)
df2['Suggestion'] = df2['Suggestion'].apply(lemmatize)

size = [60, 50, 40, 35, 30, 25, 20, 15, 10, 10]
#--------------------------------------------------------------------------------------------------------------------------
a = df2['Complain'].tolist() #converting complain column to list
b = sum(len(line.split()) for line in a) #getting the total number of words using sum
c = len(set(a)) #getting unique words
#getting the average length of sentence
sentences = [[]]
ends = set(",\n")
for word in a:
    if word in ends: sentences.append([])
    else: sentences[-1].append(word)

if sentences[0]:
    if not sentences[-1]: sentences.pop()
    d = sum(len(s) for s in sentences)/len(sentences)

dict = {
    'Total number of words': b,
    'Unique words':c,
    'Average number of words per sentence' : d
    
}
df3 = pd.DataFrame(dict,index = ['Complain'])
a = df2['Complain'].str.lower().str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)#tokenizing sentences
word_dist = nltk.FreqDist(words)#finding the frequency dsitribution 

top_N = 10 #getting the top 5 most repetitive words
rslt1 = pd.DataFrame(word_dist.most_common(top_N),columns=['Word', 'Frequency'])

fig1 = go.Figure(data =[go.Scatter(
        x=rslt1.index, 
        y=rslt1['Frequency'],
        text=rslt1['Word'],
        textposition = 'top center',
        mode = 'markers',
        marker = {
            'size' : [15000,9000,6000,4000,4000,2000,1500,1000,1000,500],
            'color': ['aqua','black','chocolate','grey','green','yellow','hotpink','purple','red','orange']
        }
                  
)] ) 


fig1.update_traces(mode='markers', marker={'sizemode':'area'})
fig1.update_layout(title='Frequency Distribution', paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)')

#-------------------------------------------------------------------------------------------------------------------------------------------


e = df2['Feedback'].tolist() #converting complain column to list
f = sum(len(line.split()) for line in e) #getting the total number of words using sum
g = len(set(e)) #getting unique words
#getting the average length of sentence
sentences = [[]]
ends = set(",\n")
for word in e:
    if word in ends: sentences.append([])
    else: sentences[-1].append(word)

if sentences[0]:
    if not sentences[-1]: sentences.pop()
    h = sum(len(s) for s in sentences)/len(sentences)

dict = {
    'Total number of words': f,
    'Unique words':g,
    'Average number of words per sentence' : h
    
}

df4 = pd.DataFrame(dict,index = ['Feedback'])

a = df2['Feedback'].str.lower().str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)#tokenizing sentences
word_dist = nltk.FreqDist(words)#finding the frequency dsitribution


top_N = 10#getting the top 5 most repetitive words
rslt2 = pd.DataFrame(word_dist.most_common(top_N),columns=['Word', 'Frequency'])

fig2 = go.Figure(data =[go.Scatter(
        x=rslt2.index, 
        y=rslt2['Frequency'],
        text=rslt2['Word'],
        textposition = 'top center',
        mode = 'markers',
        marker = {
            'size' : [15000,9000,6000,6000,4000,2000,2000,1000,1000,1000],
            'color': ['aqua','black','chocolate','grey','green','yellow','hotpink','purple','red','orange']
        }
                  
)] ) 


fig2.update_traces(mode='markers', marker={'sizemode':'area'})
fig2.update_layout(title='Frequency Distribution', paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)')


#-------------------------------------------------------------------------------------------------------------------------------------------


i = df2['Suggestion'].tolist() #converting complain column to list
j = sum(len(line.split()) for line in i) #getting the total number of words using sum
k = len(set(i)) #getting unique words
#getting the average length of sentence
sentences = [[]]
ends = set(",\n")
for word in i:
    if word in ends: sentences.append([])
    else: sentences[-1].append(word)

if sentences[0]:
    if not sentences[-1]: sentences.pop()
    l = sum(len(s) for s in sentences)/len(sentences)

dict = {
    'Total number of words': j,
    'Unique words':k,
    'Average number of words per sentence' : l
    
}

df5 = pd.DataFrame(dict,index = ['Suggestion'])
a = df2['Suggestion'].str.lower().str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)#tokenizing sentences
word_dist = nltk.FreqDist(words)#finding the frequency dsitribution


top_N = 10#getting the top 5 most repetitive words
rslt3 = pd.DataFrame(word_dist.most_common(top_N),columns=['Word', 'Frequency'])

fig3 = go.Figure(data =[go.Scatter(
        x=rslt3.index, 
        y=rslt3['Frequency'],
        text=rslt3['Word'],
        textposition = 'top center',
        mode = 'markers',
        marker = {
            'size' : [15000,9000,9000,9000,9000,4000,4000,4000,4000,4000],
            'color': ['aqua','black','chocolate','grey','green','yellow','hotpink','purple','red','orange']
        }
                  
)] ) 


fig3.update_traces(mode='markers', marker={'sizemode':'area'})
fig3.update_layout(title='Frequency Distribution', paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)')
#-------------------------------------------------------------------------------------------------------------------------------------------
layout = html.Div([
#---------------------------------------------------------------------------------------------------------------------------------------------
    html.Br(),
    html.Br(),
    html.H1("Complain Section : ",style={'textAlign':'center',"fontSize": "150%","color":"purple","font-weight":"bold"}),

    html.Br(),
    html.Br(),

    html.Div([

        dash_table.DataTable(

            id='table',
            columns=[{"name": i, "id": i} for i in df3.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'
    },

            data=df3.to_dict('records'),
        ),

    ],className = 'six-columns'),

    html.Br(),
    html.Br(),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in rslt1.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'},

            data=rslt1.to_dict('records'),
        ),      

    ],className = 'six-columns'),


    dcc.Graph(figure=fig1),

    html.Br(),
    html.Br(),
    #----------------------------------------------------------------------------------------------------------------------------------------------

    html.H1("Feedback Section : ",style={'textAlign':'center',"fontSize": "150%","color":"purple","font-weight":"bold"}),

    html.Br(),
    html.Br(),

    html.Br(),
    html.Br(),

    html.Div([

        dash_table.DataTable(

            id='table',
            columns=[{"name": i, "id": i} for i in df4.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'
    },

            data=df4.to_dict('records'),
        ),

    ],className = 'six-columns'),

    html.Br(),
    html.Br(),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in rslt2.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'},

            data=rslt2.to_dict('records'),
        ),

    ],className = 'six-columns'),

    dcc.Graph(figure=fig2),

    

#---------------------------------------------------------------------------------------------------------------------------------------------

    html.Br(),
    html.Br(),
    html.H1("Suggestion Section : ",style={'textAlign':'center',"fontSize": "150%","color":"purple","font-weight":"bold"}),

    html.Br(),
    html.Br(),

    html.Br(),
    html.Br(),

    html.Div([

        dash_table.DataTable(

            id='table',
            columns=[{"name": i, "id": i} for i in df5.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'
    },

            data=df5.to_dict('records'),
        ),

    ],className = 'six-columns'),

    html.Br(),
    html.Br(),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in rslt3.columns],
            style_as_list_view=True,
            style_cell={'fontWeight': 'bold','textAlign':'center','backgroundColor': 'white','color': 'purple','whiteSpace': 'normal','height': 'auto'},
            style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold',
                'color':'purple'},

            data=rslt3.to_dict('records'),
        ),

    ],className = 'six-columns'),

    dcc.Graph(figure=fig3),

    


])
