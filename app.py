

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



app.layout =html.Div(children=[

    html.Div(children=[
html.Img(src='https://raw.githubusercontent.com/thierryzard/thierryzard/master/logo_dgw_trans.png',
         style={
             'height': '10%',
             'width': '10%',
             'textAlign': 'left',
             'float':'left'}),
        html.H1('Corona in Nederland'),
        html.H5("automatisch geüpdatet op  {:%d/%m/%Y}".format(laatste_update)),

    ],
        style={
            'color': '#FFFFFF',
            'backgroundColor':'#203760',
            'font-family':'Rubik',
            'textAlign': 'center',
        },
    ),





          html.Div(className='row',
                 children=[
                    html.Div(className='four columns div',
                             style={
                                    'textAlign': 'left',
                                    'color': '#FFFFFF',
                                    'backgroundColor': '#8a94a6','height': '100%',


                                    },
                             children=[html.Div(

                                 html.H3(['De cijfers.']),
                                 style={'textAlign': 'center',
                                        },
 ),


                                 html.Div(html.H6([
'''Gedurende deze corona-crisis wordt over de gehele wereld allerlei data bijgehouden. Denk maar aan verpsreiding, '
aantal Geïnfecteerd, aantal doden etc. Om hier een overzicht van te krijgen is dit dashboard gecreerd.
'verschillende grafieken geven huidige cijfers betreffende corona in Nederland overzichtelijk weer.''',
html.Br(),
html.Br(),
html.Br(),
'Op dit moment bevat het Dashboard:',
html.Br(),
dcc.Markdown('''- _Aantal mensen positief getest voor corona per leeftijdsgroep in Nederland._'''),
html.Br(),
dcc.Markdown('''- _Man/Vrouw verdeling positief getest voor corona._'''),
html.Br(),
html.Br(),
]),
style={'textAlign': 'left',
       'margin-left': '15%',
       'margin-right': '15%',
       'font-family': 'Rubik',
       },),
                                     html.Div([html.P(['Dit Dashboard is gemaakt door ',
       html.A('Thierry van Zundert, ', href='https://www.digitalewereld.nl/young-professionals/thierry-van-zundert', style={'color': '#FFFFFF'}),
       'werkzaam bij ',
       html.A('Trainee.nl ', href='https://www.trainee.nl',style={'color': '#FFFFFF'}),
     'detachering bureau gespecialiseerd in business analytics & data science',
html.Br(),
html.Br(),
html.Br(),
html.Br(),
       ],
       style={'fontSize':20,
              'textAlign': 'left',
              'margin-left': '5%',
              'margin-right': '5%%',
'font-family': 'Rubik',
              'fontSize':15,

              })])





                             ]

                             ),
                    html.Div(className='eight columns',
                             children=[dcc.Tabs([ dcc.Tab(label='Corona per leeftijfdgroep', children=[
                                 dcc.Graph(id='leeftijd',figure=fig2),]),
                                 dcc.Tab(label='Man/Vrouw verdeling', children=[
                                 dcc.Graph(id='Man/Vrouw verdeling',figure=fig1),])
                                     ])])



                              ]),



])






if __name__ == '__main__':
    app.run_server(debug=True)


