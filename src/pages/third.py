import dash
from dash import dcc, html

dash.register_page(__name__, name='To-do List')

todo = ['Compare change in rate and split after stride. Think about presenting in a table or in a graph instead. Maybe '
        'highlight 5 strokes after stride on graph and then have text output below.',
        'Find a way to plot piece comparison against distance and time and not just stroke rate',
        'Deal with the fact that pieces less than the sum of the draw+winds+burn strokes gives errors. Maybe add '
        'error message or make built-in prevention message',
        'Add overview of all outings with distance rowed, average/max/min splits and plot per day. Perhaps add a '
        'total distance and average/max/min split for all training so far.',
        'why the fuck is the legend for a line showing 3 strokes after that line is finished...']

layout = html.Div(
    [
        dcc.Markdown('Things to add later!'),
        html.Div(
            className="trend",
            children=[
                html.Ul(id='my-list', children=[html.Li(i) for i in todo])
            ],
        )
    ]
)
