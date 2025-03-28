# Imports --------------------------------------------------------------------------------------------------------------
from dash import dcc, html

# Sections -------------------------------------------------------------------------------------------------------------

header = html.Div(
    [
        html.H1("Course Project"),
        html.H4("Joshua Nielsen")
    ],
    style={"text-align": "center"}
)

body = html.Div(
    [
        dcc.Dropdown(
            options=[
                {"label": "Materials Generated", "value": 0},
                {"label": "Materials Recycled", "value": 1},
                {"label": "Materials Combusted", "value": 2},
                {"label": "Materials Landfilled", "value": 3}
            ],
            value=0,
            id="material_fate_dropdown"
        ),
        dcc.Graph(id="material_fate_graph")
    ]
)

footer = html.Div(
    [
        html.P("This is a footer")
    ]
)


# Layout ---------------------------------------------------------------------------------------------------------------
def create_layout():
    return html.Div(
        [
            header,
            body,
            footer,
        ]
    )
