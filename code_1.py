import plotly.figure_factory as ff
import pandas as pd
import csv 
df = pd.read_csv('P108(2).csv')

fig = ff.create_distplot([df['Mobile Brand'].tolist()],['Mobile Brand'],show_hist=False)
fig = ff.create_distplot([df['Avg Rating'].tolist()],['Average'],show_hist=False)
fig.show()