from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px
app = Dash(__name__)

df = pd.read_csv('Cleaned_Laptop_data.csv')

group_df = df.groupby(['brand'])['brand'].count().reset_index(name = 'total')\
    .sort_values(['total'], ascending = False)

fig = px.bar(x=group_df['brand'], y=group_df['total'])

app.layout = html.Div([
    dcc.Dropdown(id='brand_selector',
                 options=[{'label': i, 'value': i} for i in df['brand'].unique()],
                 value=group_df['brand'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Brands To Filter By'),
    dcc.Graph(id='graph',
        figure={}
        )
    ])
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='brand_selector', component_property='value')]
)
def update_graph(brand_selected):
    if len(brand_selected) > 0:
        dff = group_df[group_df['brand'].isin(brand_selected)]
        fig = px.bar(group_df, x=dff['brand'], y=dff['total'])

        return fig
    else:
        fig = px.bar(x=group_df['brand'], y=group_df['total'])
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
