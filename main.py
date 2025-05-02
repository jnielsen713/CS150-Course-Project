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

list_of_years = [0, 1960, 1970, 1980, 1990, 2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
material_names = generated_df["Materials"].tolist()


# Functions ------------------------------------------------------------------------------------------------------------
def make_msd(value):
    df = material_fate_dfs[value]
    options = []
    counter = 0

    for material in df["Materials"]:
        options.append({"label": material, "value": counter})
        counter += 1

    return options


def make_mfg(value, traces):
    df = material_fate_dfs[value]
    mat_index = len(df)

    # print(material_names)
    df_flop = df.transpose()

    # print(df_flop.head(1))
    # print(df.head(1))
    fig = go.Figure()

    for t in traces:
        fig.add_trace(
            go.Scatter(
                x=list_of_years,
                y=df_flop[t],
                mode="lines",
                name=material_names[t]
            )
        )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Tons",

    )

    fig.update_xaxes(autorangeoptions_minallowed=1960, autorange=True)
    fig.update_yaxes(rangemode="tozero")

    return fig


def make_mfb(traces, year):
    # Bar Chart color & Style borrowed from Dash Documentation
    colors = ['dodgerblue', 'gray',
              'orange', 'rgba(164, 163, 204, 0.85)',
              'rgba(190, 192, 213, 1)']

    percentages = {
        "Recycled": [],
        "Landfilled": [],
        "Combusted": []
    }

    selected_materials = []
    for trace in traces:
        selected_materials.append(material_names[trace])

    for material in selected_materials:
        generated_row = generated_df[generated_df["Materials"] == material]
        recycled_row = recycled_df[recycled_df["Materials"] == material]
        landfilled_row = landfilled_df[landfilled_df["Materials"] == material]
        combusted_row = combusted_df[combusted_df["Materials"] == material]

        if generated_row.empty:
            total = 0
        else:
            total = generated_row[str(year)].values[0]

        if total > 0:
            recycled = recycled_row[str(year)].values[0] if not recycled_row.empty else 0
            landfilled = landfilled_row[str(year)].values[0] if not landfilled_row.empty else 0
            combusted = combusted_row[str(year)].values[0] if not combusted_row.empty else 0

            percentages["Recycled"].append(100 * recycled / total)
            percentages["Landfilled"].append(100 * landfilled / total)
            percentages["Combusted"].append(100 * combusted / total)
        else:
            percentages["Recycled"].append(0)
            percentages["Landfilled"].append(0)
            percentages["Combusted"].append(0)

    traces = []
    color_counter = 0
    for label in ["Recycled", "Landfilled", "Combusted"]:
        traces.append(
            go.Bar(
                x=percentages[label],
                y=selected_materials,
                marker=dict(
                    color=colors[color_counter],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                ),
                name=label,
                orientation='h',
                text=percentages[label],
                texttemplate='%{text:.1f}%',
                textposition='inside',
                insidetextanchor='middle'
            )
        )
        color_counter += 1

    layout = go.Layout(
        barmode="stack",
        xaxis={"title": "Percentage", "range": [0, 100]},
        yaxis={"title": "Material"},
        title="Material Breakdown in " + str(year) + " (as % of Total Generated)",
        height=600,
        legend=dict(orientation="h", x=0, y=1.1)
    )

    return {"data": traces, "layout": layout}



def make_dt(value):
    df = material_fate_dfs[value]
    data = df.to_dict('records')
    return data


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME],
)
