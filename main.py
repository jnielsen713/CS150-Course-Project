# Imports --------------------------------------------------------------------------------------------------------------
import pandas as pd
from dash import Dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

generated_df = pd.read_csv("data/Table 1 - Materials generated.csv")
recycled_df = pd.read_csv("data/Table 2 - Materials recycled.csv")
combusted_df = pd.read_csv("data/Table 3 - Material combusted.csv")
landfilled_df = pd.read_csv("data/Table 4 - Materials landfilled.csv")

material_fate_dfs = [generated_df, recycled_df, combusted_df, landfilled_df]

# Functions ------------------------------------------------------------------------------------------------------------
def make_mfg(value):
    df = material_fate_dfs[value]
    fig = go.Figure()
    return fig



app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME],
)

