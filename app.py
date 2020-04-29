




import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


if __name__ == '__main__':
    app.run_server(debug=True)
