import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('Cleaned_Laptop_data.csv ')
group_df = df.groupby(['ssd'])['ssd'].count().reset_index(name = 'total')\
    .sort_values(['total'], ascending = True)

# Preparing data
data = [go.Scatter(x=group_df['ssd'], y=group_df['total'])]

# Preparing layout
layout = go.Layout(title='Laptop sales based on size of SSD', xaxis_title="SIZE of MEM",
                   yaxis_title="Amount sold")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')