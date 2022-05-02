from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('Cleaned_Laptop_data.csv')

fig = px.scatter(df, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                 hover_data=['brand', 'model'])

app.layout = html.Div([
    dcc.Dropdown(id='brand_selector',
                 options=[{'label': i, 'value': i} for i in df['brand'].unique()]
                         + [{'label': 'Select All', 'value': 'allBrand'}],
                 value=df['brand'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Brands To Filter By'),
    dcc.Dropdown(id='model_selector',
                 options=[{'label': i, 'value': i} for i in df['model'].unique()]
                         + [{'label': 'Select All', 'value': 'allModel'}],
                 value=df['model'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Models To Filter By'),
    dcc.Graph(id='graph',
              figure={}
              )
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='brand_selector', component_property='value')],
    [Input(component_id='model_selector', component_property='value')]

)
def update_graph(brand_selected, model_selector):
    if (len(brand_selected) > 0) | (len(model_selector) > 0):
        if 'allBrand' in brand_selected:
            dff = df
        elif (len(brand_selected) < 1):
            dff=df
        else:
            dff = df[df['brand'].isin(brand_selected)]
        if 'allModel' in model_selector:
            dff = dff
        elif (len(model_selector) < 1):
            dff=df
        else:
            dff = dff[dff['model'].isin(model_selector)]

        fig = px.scatter(dff, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                         hover_data=['brand', 'model'])

        return fig
    else:
        fig = px.scatter(df, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                         hover_data=['brand', 'model'])
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
