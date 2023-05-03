import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('iris.csv')
print(df.columns)

trace0=go.Box(y=df[df['variety']=='Setosa']['sepal.length'],name='Setosa')

trace1=go.Box(y=df[df['variety']=='Versicolor']['sepal.length'],name='Versicolor')

trace2=go.Box(y=df[df['variety']=='Virginica']['sepal.length'],name='Virginica')

data=[trace0,trace1,trace2]
layout=go.Layout(title='Petalos de sal',xaxis=dict(title='tipo de flor'))
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Box.html')