

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import dash



# Titels
mytitle = 'piemel'
tabtitle = 'test1'
myheading = 'Mijn Dashboard'

# binnen halen URL data
url_sex = 'https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_sex.csv'
df_sex = pd.read_csv(url_sex)

# selecteerd laatste datum
pd.to_datetime(df_sex['Datum'])
recent_datum = df_sex['Datum'].max()
recent_df = df_sex[df_sex['Datum'] == recent_datum]
laatste_update = pd.to_datetime(recent_datum)

# split vrouwen/mannen
man = recent_df[recent_df["Geslacht"] == 'Man']
vrouw = recent_df[recent_df["Geslacht"] == 'Vrouw']

# plot figuur mannen vrouwen
fig1 = go.Figure(data=[
    go.Bar(name='Man', x=man['Type'], y=man['Aantal'], marker_color='#5684FF'),
    go.Bar(name='Vrouw', x=vrouw['Type'], y=vrouw['Aantal'], marker_color='#E3127B')
])

# plot tekst en layout mannen vrouwen
fig1.update_layout(
    title={
        'text': "Man/Vrouw verdeling positief getest voor corona",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    titlefont_size=30,
    autosize=True,
    barmode='group',
    yaxis_title="Aantal Mensen positief voor corona",
    plot_bgcolor='#f5f7fa',
    # x-axis
    xaxis=dict(
        {'categoryorder': 'array', 'categoryarray': ['Ziekenhuisopname', 'Overleden', 'Totaal']},
        tickfont_size=14
    ),
    # y-axis
    yaxis=dict(
        title="Aantal mensen positief getest",
        titlefont_size=18,
        tickfont_size=14
    ),
    # balken
    bargap=0.6,
    bargroupgap=0.1,
    # legenda
    legend=dict(
        x=0.1,
        y=1.0,
        bgcolor='white',
        bordercolor='black',
        borderwidth=1,
        font=dict(
            size=12,
            color="#000000"
        )
    )
)

# aanpassen aan grote
fig1.update_yaxes(automargin=True)
fig1.update_xaxes(automargin=True)

# binnen halen URL data
url_age = 'https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_age.csv'
df_age = pd.read_csv(url_age)

# selecteerd laatste datum
pd.to_datetime(df_age['Datum'])
recent_datum2 = df_age['Datum'].max()
recent_df2 = df_age[df_age['Datum'] == recent_datum]
laatste_update2 = pd.to_datetime(recent_datum)

# split df in df per type
df_overleden = recent_df2[recent_df2['Type'] == "Overleden"]
df_ziekenhuis = recent_df2[recent_df2['Type'] == "Ziekenhuisopname"]
df_totaal = recent_df2[recent_df2['Type'] == "Totaal"]

# plot per type
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=recent_df2['LeeftijdGroep'],
                          y=df_ziekenhuis['Aantal'],
                          name='Ziekenhuis',
                          marker_color='#a72f6e ',
                          mode='lines+markers'
                          ))
fig2.add_trace(go.Scatter(x=recent_df2['LeeftijdGroep'],
                          y=df_overleden['Aantal'],
                          name='Overleden',
                          marker_color='#203760',
                          mode='lines+markers',
                          ))
fig2.add_trace(go.Scatter(x=recent_df2['LeeftijdGroep'],
                          y=df_totaal['Aantal'],
                          name='Totaal',
                          marker_color='#dca108',
                          mode='lines+markers',
                          ))

# plot layout
fig2.update_layout(
    plot_bgcolor='#f5f7fa',
    title={
        'text': 'Aantal mensen positief getest voor corona per leeftijdsgroep in Nederland',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    titlefont_size=30,
    autosize=True,
    xaxis=dict(
        title="Leeftijd",
        titlefont_size=14,
        tickfont_size=14,
        tickangle=-45
    ),
    yaxis=dict(
        title="Aantal mensen positief getest",
        titlefont_size=14,
        tickfont_size=14
    ),

    legend=dict(
        x=0.1,
        y=1.0,
        bgcolor='white',
        bordercolor='black',
        borderwidth=1,
        font=dict(
            size=12,
            color="#000000"
        )
    ))

# aanpassen aan grote
fig2.update_yaxes(automargin=True)
fig2.update_xaxes(automargin=True)




########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.title = tabtitle

########### Set up the layout
colors = {
    'background': '#203760',
    'text': '#FFFFFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children = 'Corona in Nederland',
               style = {
    'textAlign': 'center',
    'color': colors['text']
}
),
html.Div(children=f'automatisch geüpdatet op:{laatste_update} ', style={
    'textAlign': 'center',
    'color': colors['text']
}),



    dcc.Graph(
        id='flyingdog',
        figure=fig1),
    dcc.Graph(
        id='flyingdog2',
        figure=fig2
)
]
)




if __name__ == '__main__':
    app.run_server(debug=True)


