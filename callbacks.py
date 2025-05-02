from main import app, make_mfg, make_msd, make_mfb, make_dt
from dash import dcc, Output, Input, State


def register_callbacks(app):

    @app.callback(Output("visual_one_mat_select", "options"),
                  Output("visual_one_mat_select", "value"),
                  Input("visual_one_dropdown", "value"),
                  State("visual_one_mat_select", "value"))
    def update_visual_one_mat_selection_dropdown(value, current_selection):
        options = make_msd(value)
        # print(options)
        return options, current_selection

    @app.callback(Output("visual_one_graph", "figure"),
                  Input("visual_one_dropdown", "value"),
                  Input("visual_one_mat_select", "value"))
    def update_material_fate_graph(value, traces):
        return make_mfg(value, traces)

    @app.callback(Output("visual_two_graph", "figure"),
                  Input("visual_two_dropdown", "value"),
                  Input("visual_two_slider", "value"))
    def update_material_fate_breakdown(traces, year):
        return make_mfb(traces, year)

    @app.callback(Output("data_table", "data"),
                  Input("dataset_dropdown", "value"))
    def update_data_table(value):
        return make_dt(value)
