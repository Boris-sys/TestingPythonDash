import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        #the output is the chart itself
        Output(ids.BAR_CHART, "children"),
        [
            #this inputs define which components influence the data displayed
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ],
    )

    #this function filters the data depending on the parameters
    def update_bar_chart(
        years: list[str], months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_data = data.query(
            "year in @years and month in @months and category in @categories"
        )

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        #this function is needed to know wich data is showed based on a specific index
        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.AMOUNT,
                index=[DataSchema.CATEGORY],
                aggfunc="sum",
                fill_value=0,
                dropna=False,
            )
            return pt.reset_index().sort_values(DataSchema.AMOUNT, ascending=False)

        #declaration of the chart that will be returned later
        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)