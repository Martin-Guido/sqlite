import dash
from dash import dcc
from dash import html, Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import json

df=pd.read_csv('auto-mpg.csv')
df['year']=df['model year'] + np.random.randint(-4,5,df.shape[0])*0.10

app=dash.Dash()

app.layout=html.Div([html.Div([dcc.Graph(id='mpg_scatter'
										,figure={'data':[go.Scatter(x=df['year']+1900,
																		 y=df['mpg'],
																		 text=df['car name'],
																		 hoverinfo='text',
																		 mode='markers')],
									'layout':go.Layout(title='dataset mpg',
													xaxis={'title':'model_year'}
												, yaxis={'title':'miles per gallon'},
												 hovermode='closest')})],
										style={'width':'50%', 'display':'inline-block'}), 
					html.Div([dcc.Graph(id='mpg_line'
						, figure={'data':[go.Scatter(x=[0,1],y=[0,1], mode='lines')],
						 'layout':go.Layout(title='acceleration',margin={'l':0})}), 
					dcc.Markdown(id='mpg_stats')], style={'width':'20%','heigth':'50%', 'display':'inline-block'})])

@app.callback(Output(component_id='mpg_line',component_property='figure'),
			[Input(component_id='mpg_scatter',component_property='clickData')])
def callback_graph(clickData):
	v_index=clickData['points'][0]['pointIndex']
	fig={'data':[go.Scatter(x=[0,1],
							y=[0,60/df.iloc[v_index]['acceleration']],
							mode='lines',
							line={'width':2*df.iloc[v_index]['cylinders']})], 
		'layout':go.Layout(title=df.iloc[v_index]['car name'],
							xaxis={'visible':False},yaxis={'visible':False,'range':[0,60/df['acceleration'].min()]},
							margin={'l':0}, heigth=300)}


	return fig





@app.callback(Output(component_id='mpg_stats',component_property='children'),
			[Input(component_id='mpg_scatter',component_property='clickData')])
def callback_stats(clickData):

	v_index=clickData['points'][0]['pointIndex']
	stats="""
		{} cylinders/n
		{} cc displascement
		 0 to 60mph in {} seconds""".format(df.iloc[v_index]['cylinders'],
		 									df.iloc[v_index]['displacement'],
		 									df.iloc[v_index]['acceleration'])
	return stats

if __name__ == '__main__':
	app.run_server()