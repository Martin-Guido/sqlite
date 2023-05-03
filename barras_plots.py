import pandas as pd
import sqlite3
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

salida=pd.read_csv('Winter.csv', sep= ',')
con=sqlite3.connect('Winter.db')
salida.to_sql('year',con,if_exists='replace', index=False)

cursor=con.cursor()
consulta='SELECT * FROM year'
salida=pd.read_sql(consulta,con)
print(salida.columns)

consulta1='SELECT Country_Code, Gold, Silver, Bronze FROM year WHERE Year=2018'
cursor.execute(consulta1)
filas=cursor.fetchall()
#for fila in filas:
#print(np.array(filas).T[0])

con.close()

trace0=go.Bar(x=np.array(filas).T[0],
					y=np.array(filas).T[1],
					name='Oro'
					,marker={'color':'#FFD700'})

trace1=go.Bar(x=np.array(filas).T[0],
					y=np.array(filas).T[2],
					name='plata'
					,marker={'color':'#9EA7A1'})
trace2=go.Bar(x=np.array(filas).T[0],
					y=np.array(filas).T[3],
					name='Bronze'
					,marker={'color':'#CD7F32'})
data=(trace0,trace1,trace2)

layout=go.Layout(title='Medallas por pais',barmode='stack')
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='Medallasbarras.html')