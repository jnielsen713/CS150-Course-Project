from main import app, make_mfg
from dash import dcc, Output, Input, State



@app.callback(Output("material_fate_graph", "figure"),
              Input("material_fate_dropdown", "value"))
def update_material_fate_graph(value):
    return make_mfg(value)