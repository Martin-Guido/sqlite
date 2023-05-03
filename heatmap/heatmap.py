import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly import subplots

dfCA=pd.read_csv('2010SantaBarbaraCA.csv')
dfAK=pd.read_csv('2010SitkaAK.csv')
dfAZ=pd.read_csv('2010YumaAZ.csv')
print(dfAZ.columns)

trace0=go.Heatmap(x=dfAZ['DAY'],
	y=dfAZ['LST_TIME'],
	z=dfAZ['T_HR_AVG'].values.tolist(),colorscale='JET',zmin=0,zmax=45)

trace1=go.Heatmap(x=dfAK['DAY'],
	y=dfAK['LST_TIME'],
	z=dfAK['T_HR_AVG'].values.tolist(),colorscale='Jet',zmin=0,zmax=45)


trace3=go.Heatmap(x=dfCA['DAY'],
	y=dfCA['LST_TIME'],
	z=dfCA['T_HR_AVG'].values.tolist(),colorscale='Jet',zmin=0,zmax=45)


fig=subplots.make_subplots(rows = 1, cols = 3, subplot_titles = ['Sitka AK', 'Santa Barbara CA','Yuma AZ'],
	y_title = 'Hourly Avg Temp', shared_yaxes = True)

fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,2)
fig.append_trace(trace3,1,3)
fig.update_layout(title='mapa de calor',title_x = 0.5)
fig.show()
pyo.plot(fig,filename='Heatmap.html')