import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Cleaned_Laptop_data.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

group_df = df.groupby(['processor_brand'])['processor_brand'].count().reset_index(name = 'total')\
    .sort_values(['total'], ascending = False)

# Preparing data


# Preparing layout
layout = go.Layout(title='Number of Laptops by Brand', xaxis_title="Brand",
                   yaxis_title="Number of Laptops")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')
