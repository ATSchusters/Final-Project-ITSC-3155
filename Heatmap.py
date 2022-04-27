import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'max'}).reset_index()

# Preparing data

data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['average_min_temp'].values.tolist(),
                   colorscale='Jet')]
# Preparing layout
layout = go.Layout(title='Max Temperature of Each Day of The Week by Month',
                   xaxis_title="Day of The Week",
                   yaxis_title="Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherheatmap.html')