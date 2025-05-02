# Imports --------------------------------------------------------------------------------------------------------------
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

# Components

info_card = dbc.Card(
    [
        html.H1("Welcome!"),
        html.Img(src="/assets/recycle_truck.jpg", className="text_img"),
        html.Br(),
        html.P("We've been told to be mindful of our waste our whole lives. Trash, compost, and recycling should all be separated, and are dealt with accordingly. Sounds easy, right? Well..."),
        html.Br(),
        html.P(html.A("Over 50% of americans admit to a lack of confidence when it comes to recycling.", href="https://www.waste360.com/waste-recycling/covanta-survey-americans-don-t-know-how-to-recycle-"), className="big_stat"),
        html.Br(),
        html.P("Whether it's out in public, or in their own homes, people can get caught up over where to put their waste. They think through what it might be made of, and where it came from, but might be unable to confidently place it in a bin. The confusing labels aren't helping one bit! The point of this dashboard is to help clear up certain confusions about recycling, and to shed a light on how waste management actually works.")

    ],
    className="card"
)

visual_one = dbc.Card(
    [
        html.P("Which graph would you like to see?"),
        dcc.Dropdown(
            options=[
                {"label": "Materials Generated", "value": 0},
                {"label": "Materials Recycled", "value": 1},
                {"label": "Materials Combusted", "value": 2},
                {"label": "Materials Landfilled", "value": 3}
            ],
            value=0,
            id="visual_one_dropdown"
        ),
        html.Br(),
        html.P("Which material(s) would you like to see on the graph?"),
        dcc.Dropdown(
            options=[
                {"label": "temp", "value": 0},
                {"label": "temporary", "value": 1}
            ],
            multi=True,
            value=[0, 1, 5, 6],
            id="visual_one_mat_select"
        ),
        dcc.Graph(id="visual_one_graph"),
        html.P("This visual depicts the various fates that waste faces when it reaches the end of it's life cycle. It is either recycled, (yay!) landfilled, (boo!) or combusted. You can also see how much of each material was generated. Use the dropdown to pick which fate to examine, and pick and choose your favorite materials to compare them. It isn't indexxed or anything, so keep in mind that items that were produced in greater quantities will be recycled/landfilled/combusted in larger quantities. A breakdown for each material can be found on the next tab.")
    ],
    className="card"
)

visual_two = dbc.Card(
    [
        html.P("Which material(s) would you like to see?"),
        dcc.Dropdown(
            options=[
                {"label": "Paper and Paperboard", "value": 0},
                {"label": "Glass", "value": 1},
                {"label": "Metals - Ferrous", "value": 2},
                {"label": "Metals - Aluminum", "value": 3},
                {"label": "Metals - Other Nonferrous", "value": 4},
                {"label": "Metals - Total", "value": 5},
                {"label": "Plastics", "value": 6},
                {"label": "Rubber and Leather", "value": 7},
                {"label": "Textiles", "value": 8},
                {"label": "Wood", "value": 9},
                {"label": "Other", "value": 10},
                # {"label": "Total Materials"},
                # {"label": "Food Waste"},
                # {"label": "Yard Trimmings"},
                # {"label": "Miscellaneous Inorganic Wastes"},
                # {"label": "Total"},
                # {"label": "Weight"},
            ],
            multi=True,
            value=[0],
            id="visual_two_dropdown"
        ),
        html.Br(),
        html.P("What year would you like to break down?"),
        dcc.Slider(
            min=1960,
            max=2018,
            marks={1960: "1960", 1970: "1970", 1980: "1980", 1990: "1990", 2000: "2000", 2005: "2005", 2010: "'10", 2011: "'11", 2012: "'12", 2013: "'13", 2014: "'14", 2015: "'15", 2016: "'16", 2017: "'17", 2018: "'18"},
            value=2000,
            step=None,
            id="visual_two_slider"
        ),
        dcc.Graph(id="visual_two_graph"),
        html.P("This visual breaks down the individual materials and shows what percentage of that material met each fate for a given year. When you play around with this one you can really see when the recycling infrastructure was developed. Since 2010, not a whole lot has changed. It's cool to see which materials are more likely to be recycled, or combusted as well. Paper/Paperboard and leather/rubber are great examples of that, respectively. Add as many materials to the chart as you'd like using the dropdown menu!")
    ],
    className="card"
)

visual_three = dbc.Card(
    [
        html.P("This is the card with the third visual. It might be a world map, or even a pie chart! who knows..."),
        html.P("...I guess it's lost media now!"),
        dcc.Graph(id="visual_three_graph"),
        html.P("Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.")
    ],
    className="card"
)

data_card = dbc.Card(
    [
        html.P("This is the card with our datasets, and information on how they were obtained."),
        html.P("Which dataset would you like to look at?"),
        dcc.Dropdown(
            options=[
                {"label": "Materials Generated (In Tons)", "value": 0},
                {"label": "Materials Recycled (In Tons)", "value": 1},
                {"label": "Materials Combusted (In Tons)", "value": 2},
                {"label": "Materials Landfilled (In Tons)", "value": 3}
            ],
            value=0,
            id="dataset_dropdown"
        ),
        dash_table.DataTable(
            data=[],
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            page_size=10,
            id="data_table"
        ),
        html.P(["These datasets are accredited to the US Environmental Protection Agency, and were downloaded from ", html.A("https://data.gov/", href="https://data.gov/"), " and were slightly modified to make it easier for pandas to read them (removing empty rows etc.)"]),
    ],
    className="card"
)

action_card = dbc.Card(
    [
        html.P("So what are we to do with this information?"),
        html.Img(src="/assets/recycle_bins.jpg", className="text_img"),
        html.Br(),
        html.P("We can see how the country has prioritized recycling over the years, and get a better understanding of which materials are favored in the process. I hope the direct comparisons are helpful! For example we can choose paper products over plastic ones, as they're more likely to be recycled."),
        html.P(["It is important to consider not only whether something can be recycled, but the likelihood that it actually will. Check your county's waste management system to see if the blue bins make it to a sorting station, or recycling plant. ", html.A("Here in Santa Barbara county", href="https://sustainability.santabarbaraca.gov/utilities/trash-recycling"), ", recycling is pretty good. Although I can't confirm that our school's big blue dumpsters make it all the way, there is a good chance."]),
        html.Br(),
        html.P(html.A("Only 21% of household recycling is actually properly recycled", href="https://recyclingpartnership.org/report-shows-only-21-of-u-s-residential-recyclables-are-captured-points-to-policy-and-investment-as-immediate-solutions/"), className="big_stat"),
        html.Br(),
        html.P("Be it the fault of the confused public, or a lack of investment due to a lack of economic incentive, not all of the recycling makes it, even if we put it in the right bin. Good steps for the future include raising awareness and focusing on the other two 'r's: Reduce and Reuse. Making the most of what material we have already generated is good for the environment, since we will always be making more. I hope this dashboard was a good tool to help you understand recycling and waste management just a little bit better!")
    ],
    className="card"
)

# Sections -------------------------------------------------------------------------------------------------------------

header = dbc.Row(
    [
        html.H1("Recycling and Waste Management Statistics", style={"color": "white"}),
        html.H4("Joshua Nielsen - CS-150 - Prof. Mike Ryu", style={"color": "lightgray"})
    ],
    style={"text-align": "center"},
    id="header",
    className="p-4 primary_section",
)

body = dbc.Row(
    [
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        info_card
                    ],
                    label="Overview",
                    label_style={"color": "darkblue", "textAlign": "center"},
                    tab_style={"width": "20%"}
                ),
                dbc.Tab(
                    [
                        visual_one
                    ],
                    label="The Fates",
                    label_style={"color": "darkblue", "textAlign": "center"},
                    tab_style={"width": "20%"}
                ),
                dbc.Tab(
                    [
                        visual_two
                    ],
                    label="Material Breakdown",
                    label_style={"color": "darkblue", "textAlign": "center"},
                    tab_style={"width": "20%"}
                ),
                dbc.Tab(
                    [
                        data_card
                    ],
                    label="Datasets",
                    label_style={"color": "darkblue", "textAlign": "center"},
                    tab_style={"width": "20%"}
                ),
                dbc.Tab(
                    [
                        action_card
                    ],
                    label="Action Steps",
                    label_style={"color": "darkblue", "textAlign": "center"},
                    tab_style={"width": "20%"}
                )
            ],
            style={"display": "flex"}
        )
    ],
    className="secondary_section"
)

footer = html.Div(
    [
        html.P(["Want to learn more?", " ", html.A("Course Project Proposal", href="https://docs.google.com/document/d/1dk7CfL9lpd1Hc54wQcepS8y8t5xUyxPnZMbiB2fVXOs"), " ",  html.A(" EPA waste management dashboard", href="https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials")]),
    ],
    className="p-4 primary_section"
)


# Layout ---------------------------------------------------------------------------------------------------------------
def create_layout():
    return dbc.Container(
        [
            dbc.Row(
                header
            ),
            dbc.Row(
                body
            ),
            dbc.Row(
                footer
            )
        ],
        fluid=True
    )
