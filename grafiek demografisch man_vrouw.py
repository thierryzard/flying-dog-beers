#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import modules
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import io
import requests
import dash
import dash_core_components as dcc
import dash_html_components as html


#binnen halen URL data
url_sex = 'https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_sex.csv'
source_sex = requests.get(url_sex).content
df_sex = pd.read_csv(io.StringIO(source_sex.decode('utf-8')))


#selecteerd laatste datum
pd.to_datetime(df_sex['Datum'])
recent_datum = df_sex['Datum'].max()
recent_df= df_sex[df_sex['Datum']== recent_datum]
laatste_update = pd.to_datetime(recent_datum)


#split vrouwen/mannen
man= recent_df[recent_df["Geslacht"]== 'Man']
vrouw= recent_df[recent_df["Geslacht"]== 'Vrouw']

#plot figuur
fig = go.Figure(data=[
    go.Bar(name='Man', x=man['Type'], y=man['Aantal'],marker_color='#5684FF'),
    go.Bar(name='Vrouw', x=vrouw['Type'], y=vrouw['Aantal'], marker_color='#E3127B')
])


# plot tekst en layout
fig.update_layout(
    title={
        'text': "Man/Vrouw verdeling positief getest voor corona",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    titlefont_size=30,
    autosize=True,
    barmode='group',
    yaxis_title="Aantal Mensen positief voor corona",
    plot_bgcolor='#f5f7fa',
    #x-axis
    xaxis=dict(
        {'categoryorder':'array', 'categoryarray':['Ziekenhuisopname', 'Overleden','Totaal']},
        tickfont_size=14
        ),
    #y-axis
    yaxis=dict(
        title="Aantal mensen positief getest",
        titlefont_size=18,
        tickfont_size=14
    ),
    #balken
    bargap=0.6,
    bargroupgap=0.1,
    #legenda
    legend=dict(
        x=0.1,
        y=1.0,
        bgcolor='white',
        bordercolor ='black',
        borderwidth = 1,
        font=dict(
            size=12,
            color="#000000"
            )
    ) 
)


#laatste update om: 
fig.add_annotation(
    dict(
            x=0.99,
            y=1,
            showarrow=False,
            text="geüpdatet op  {:%d/%m/%Y}".format(laatste_update),
            xref="paper",
            yref="paper",
        font=dict(
            size=10,
            color="#FFFFFF"
            ),
        align="center",  
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.7
))      

#aanpassen aan grote
fig.update_yaxes(automargin=True)
fig.update_xaxes(automargin=True)



app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server()



# In[ ]:




