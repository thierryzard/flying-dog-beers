import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
import pandas as pd 

#binnen halen URL data
url_sex = 'https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_sex.csv'
df_sex = pd.read_csv(url_sex)

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


########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'




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
        x=2,
        y=5,
        xref="x",
        yref="y",
        text="max=5",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )
))      

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=fig
    ),
    html.A('automatisch geüpdatet op:', laatste_update)
        ]
)

if __name__ == '__main__':
    app.run_server()
