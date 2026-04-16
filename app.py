from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f9f9f9'}, children=[
    
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', 
            inline=True,
            inputStyle={"margin-left": "20px", "margin-right": "5px"}
        ),
    ]),

    html.Div(style={'backgroundColor': 'white', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Sales Trend: {region.upper() if region else 'ALL'} Region",
        labels={"date": "Date", "sales": "Sales (USD)"},
        color_discrete_sequence=["#e84393"]
    )
    
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor='white'
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)