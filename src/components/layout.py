import pandas as pd
from dash import Dash, html
from src.components import (
    bar_chart,
    category_dropdown,
    month_dropdown,
    pie_chart,
    year_dropdown,
)


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    #This function contains the structure of the page
    #each one of the custom components contains a render function returning the desire viusual
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    #This div contains all the dropdowns
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data),
                ],
            ),
            html.H4('Bar Chart'),
            bar_chart.render(app, data),
            html.H4('Pie Chart'),
            pie_chart.render(app, data),
        ],
    )