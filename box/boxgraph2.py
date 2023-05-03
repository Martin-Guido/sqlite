import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('iris.csv')
print(df.columns)
data=[go.Box(y=df[df['variety']==flor]['sepal.length'],name=flor,boxpoints='all') 
		for flor in df['variety'].unique()]

layout=go.Layout(title='Petalos de sal',xaxis=dict(title='tipo de flor'))
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Box.html')