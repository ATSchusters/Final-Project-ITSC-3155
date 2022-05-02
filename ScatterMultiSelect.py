from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('Cleaned_Laptop_data.csv')

fig = px.scatter(df, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                 hover_data=['brand', 'model', 'processor_brand', 'processor_name', 'ram_GB', 'ram_type',
                             'ssd', 'hdd', 'os', 'weight', 'display_size', 'Touchscreen'])

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

    dcc.Dropdown(id='processor_brand_selector',
                 options=[{'label': i, 'value': i} for i in df['processor_brand'].unique()]
                         + [{'label': 'Select All', 'value': 'allProcessorBrand'}],
                 value=df['processor_brand'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Processors Brands To Filter By'),

    dcc.Dropdown(id='processor_name_selector',
                 options=[{'label': i, 'value': i} for i in df['processor_name'].unique()]
                         + [{'label': 'Select All', 'value': 'allProcessorName'}],
                 value=df['processor_name'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Processor Names To Filter By'),

    dcc.Dropdown(id='ram_selector',
                 options=[{'label': i, 'value': i} for i in df['ram_GB'].unique()]
                         + [{'label': 'Select All', 'value': 'allRam'}],
                 value=df['ram_GB'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Ram Size To Filer By'),

    dcc.Dropdown(id='ram_type_selector',
                 options=[{'label': i, 'value': i} for i in df['ram_type'].unique()]
                         + [{'label': 'Select All', 'value': 'allRamType'}],
                 value=df['ram_type'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Ram Types To Filter By'),

    dcc.Dropdown(id='ssd_selector',
                 options=[{'label': i, 'value': i} for i in df['ssd'].unique()]
                         + [{'label': 'Select All', 'value': 'allSSD'}],
                 value=df['ssd'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select SSD in GB To Filter By'),

    dcc.Dropdown(id='hdd_selector',
                 options=[{'label': i, 'value': i} for i in df['hdd'].unique()]
                         + [{'label': 'Select All', 'value': 'allHDD'}],
                 value=df['hdd'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select HDD in GB To Filter By'),

    dcc.Dropdown(id='os_selector',
                 options=[{'label': i, 'value': i} for i in df['os'].unique()]
                         + [{'label': 'Select All', 'value': 'allOS'}],
                 value=df['os'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Operating Systems To Filter By'),

    dcc.Dropdown(id='weight_selector',
                 options=[{'label': i, 'value': i} for i in df['weight'].unique()]
                         + [{'label': 'Select All', 'value': 'allWeight'}],
                 value=df['weight'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Laptop Weight To Filter By'),

    dcc.Dropdown(id='display_size_selector',
                 options=[{'label': i, 'value': i} for i in df['display_size'].unique()]
                         + [{'label': 'Select All', 'value': 'allDisplaySize'}],
                 value=df['display_size'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select Display Size To Filter By'),

    dcc.Dropdown(id='touchscreen_selector',
                 options=[{'label': i, 'value': i} for i in df['Touchscreen'].unique()]
                         + [{'label': 'Select All', 'value': 'allTouchscreen'}],
                 value=df['Touchscreen'].unique(),
                 multi=True,
                 searchable=True,
                 clearable=True,
                 placeholder='Select if Touchscreen To Filter By'),

    dcc.Graph(id='graph',
              figure={}
              )
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='brand_selector', component_property='value')],
    [Input(component_id='model_selector', component_property='value')],
    [Input(component_id='processor_brand_selector', component_property='value')],
    [Input(component_id='processor_name_selector', component_property='value')],
    [Input(component_id='ram_selector', component_property='value')],
    [Input(component_id='ram_type_selector', component_property='value')],
    [Input(component_id='ssd_selector', component_property='value')],
    [Input(component_id='hdd_selector', component_property='value')],
    [Input(component_id='os_selector', component_property='value')],
    [Input(component_id='weight_selector', component_property='value')],
    [Input(component_id='display_size_selector', component_property='value')],
    [Input(component_id='touchscreen_selector', component_property='value')]

)
def update_graph(brand_selected, model_selector, processor_brand_selector, processor_name_selector, ram_selector,
                 ram_type_selector, ssd_selector, hdd_selector, os_selector, weight_selector, display_size_selector,
                 touchscreen_selector):
    if len(brand_selected) > 0 or len(model_selector) > 0 or len(processor_brand_selector) > 0 or len(ram_selector) > 0\
            or len(processor_name_selector) > 0 or len(ram_type_selector) > 0 or len(ssd_selector) > 0\
            or len(hdd_selector) > 0 or len(os_selector) > 0 or len(weight_selector) > 0\
            or len(display_size_selector) > 0 or len(touchscreen_selector) > 0:

        dff = df
        if 'allBrand' in brand_selected:
            dff = dff
        elif len(brand_selected) < 1:
            dff = dff
        else:
            dff = dff[dff['brand'].isin(brand_selected)]

        if 'allModel' in model_selector:
            dff = dff
        elif len(model_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['model'].isin(model_selector)]

        if 'allProcessorBrand' in processor_brand_selector:
            dff = dff
        elif len(processor_brand_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['processor_brand'].isin(processor_brand_selector)]

        if 'allProcessorName' in processor_name_selector:
            dff = dff
        elif len(processor_name_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['processor_name'].isin(processor_name_selector)]

        if 'allRam' in ram_selector:
            dff = dff
        elif len(ram_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['ram_GB'].isin(ram_selector)]

        if 'allRamType' in ram_type_selector:
            dff = dff
        elif len(ram_type_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['ram_type'].isin(ram_type_selector)]

        if 'allSSD' in ssd_selector:
            dff = dff
        elif len(ssd_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['ssd'].isin(ssd_selector)]

        if 'allHDD' in hdd_selector:
            dff = dff
        elif len(hdd_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['hdd'].isin(hdd_selector)]

        if 'allOS' in os_selector:
            dff = dff
        elif len(os_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['os'].isin(os_selector)]

        if 'allWeight' in weight_selector:
            dff = dff
        elif len(weight_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['weight'].isin(weight_selector)]

        if 'allDisplaySize' in display_size_selector:
            dff = dff
        elif len(display_size_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['display_size'].isin(display_size_selector)]

        if 'allTouchscreen' in touchscreen_selector:
            dff = dff
        elif len(touchscreen_selector) < 1:
            dff = dff
        else:
            dff = dff[dff['Touchscreen'].isin(touchscreen_selector)]


        fig = px.scatter(dff, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                         hover_data=['brand', 'model','processor_brand', 'processor_name','ram_GB', 'ram_type',
                                     'ssd', 'hdd', 'os', 'weight', 'display_size', 'Touchscreen'])

        return fig
    else:
        fig = px.scatter(df, x='star_rating', y='latest_price', color='star_rating', size='latest_price',
                         hover_data=['brand', 'model','processor_brand', 'processor_name','ram_GB', 'ram_type',
                                     'ssd', 'hdd', 'os', 'weight', 'display_size', 'Touchscreen'])
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
