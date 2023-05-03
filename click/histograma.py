import pandas as pd
#import sqlite3
#import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('auto-mpg.csv')

data=[go.Histogram(x=df['mpg'],nbinsx=19,histnorm='percent')]
layout=go.Layout(title='Histograma')
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Histograma.html')