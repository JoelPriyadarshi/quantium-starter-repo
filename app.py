from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Trend (2020-2022)",
    labels={"date": "Date of Sale", "sales": "Total Sales (USD)"}
)

fig.add_vline(x="2021-01-15", line_width=3, line_dash="dash", line_color="red")
fig.add_annotation(x="2021-01-15", text="Price Increase", showarrow=True, arrowhead=1)

app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)