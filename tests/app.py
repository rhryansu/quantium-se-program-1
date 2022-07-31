# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import csv
import operator

from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# with open('pink_morsels.csv', 'r+') as inp, open("pink_morsels.csv", 'w+') as out:
#     reader = csv.reader(inp)
#     writer = csv.writer(out)
#     data = [row for row in reader]
# #     date = []
# #     sales = []
# #     region = []
#     for i in data:
#         i[0] = i[0].replace('$', '')
#         print(i)
#     # writer.writerows(data)

#         sales.append(i[0])
#         date.append(i[1])
#         region.append(i[2])
# df = pd.DataFrame({
#     "Date": date,
#     "Sales": sales,
#     "Region": region
# })
# df['Date'] = pd.to_datetime(df['Date'])
# fig = px.line(df, x="Date", y="Sales", color="Region")

df = pd.read_csv('pink_morsels.csv')
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by=['sales'])

fig = px.line(df, x="date", y="sales", color="region")


app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales by Date and Region'),

    html.Div([dcc.RadioItems(options=[{'label': 'north', 'value': 'north'},
                                      {'label': 'east', 'value': 'east'},
                                      {'label': 'south', 'value': 'south'},
                                      {'label': 'west', 'value': 'west'},
                                      {'label': 'all', 'value': 'all'}], value='all', id='region-selection')]),

    dcc.Graph(
        id='sales-by-date-graph',
        figure=fig
    ),


])


@app.callback(
    Output('sales-by-date-graph', 'figure'),
    [Input('region-selection', 'value')]
)
def update_figure(value):
    dff = pd.read_csv('pink_morsels.csv')

    if value != 'all':
        dff = dff[dff['region'] == value]
        line_fig = px.line(dff, x='date', y='sales')
    else:
        line_fig = px.line(dff, x='date', y='sales', color='region')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)
