import dash
import dash_core_components
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


# Data Exploration with Pandas

df = pd.read_csv("vgsales.csv")

# print(df[200:205])
# print(df.iloc[:5,[2,6,10]])
# print(df.loc[:5,["Platform"]])

#print(df.Platform.unique())
#print(df.Platform.nunique())

#print(sorted(df.Year.unique()))
#print(df.Year.nunique())

# Data Visualization with Plotly

#fig_pie = px.pie(data_frame=df, names='Genre', values='Japan Sales')
#fig_pie.show()

# fig_bar = px.bar(data_frame=df, x='Genre', y='Japan Sales')
# fig_bar.show()

# fig_hist = px.histogram(data_frame=df, x='Year', y='Japan Sales')
# fig_hist.show()


# Interactive Graphing with Dash

app = dash.Dash(__name__)

app.layout=html.Div([
    html.H1("Graph Analysis with Charming Data"),
    dcc.Dropdown(id='genre-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.Genre.unique())],
                 value='Action'
                 ),
    dcc.Graph(id='my-graph',
              figure={}),
])
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphs(value_genre):
    print(value_genre)
    dff = df[df.Genre==value_genre]
    fig = px.histogram(data_frame=dff, x='Year', y='Japan Sales')
    return fig


if __name__=='__main__':
    app.run_server()