import dash
from dash import dcc
from dash import html, Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import json


df=pd.read_csv('wheels.csv')


app=dash.Dash()
features=df.columns
app.layout=html.Div([html.Div([dcc.Graph(id='color-wheels',
										 figure={'data':[go.Scatter(x=df['color'],
										 	y=df['wheels'],dy=1,
										 	mode='markers',marker={'size':8,'color':'rgb(200,10,90)','line':{'width':2}})],
										 	'layout':go.Layout(title='Ruedas y colores',
										 						xaxis={'title':'color'},
										 						yaxis={'title':'# of wheels','nticks':3},
										 						hovermode='closest') })],
			style={'width':'30%','float':'left'}),
			html.Div([html.Pre(id='hover-data',style={'padding-Top':35})], style={'width':'30%'})])



					

@app.callback(Output(component_id='hover-data',component_property='children'),
			[Input(component_id='color-wheels',component_property='clickData')])

def get_hoverinfo(Hoverdata):
	return json.dumps(Hoverdata,indent=2)


if __name__ == '__main__':
	app.run_server()