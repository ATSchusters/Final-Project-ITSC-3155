import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Final-Project-ITSC-3155/Cleaned_Laptop_data.csv')

# Preparing data
data = [
    go.Scatter(x=df['star_rating'],
               y=df['latest_price'],
               text=df['model'],
               mode='markers',
               marker=dict(size=df['latest_price']/5000,color=df['star_rating'], showscale=True)
               )
]

# Preparing layout
layout = go.Layout(title='Laptop Ratings by Brand', xaxis_title="5 Star Rating",
                   yaxis_title="Latest Price", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')