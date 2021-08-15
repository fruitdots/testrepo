# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("/Users/katesweeney/Desktop/spacex_launch_dash.csv")
max_payload = spacex_df['Payload_Mass_(kg)'].max()
min_payload = spacex_df['Payload_Mass_(kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Br(),
html.Div([
                                        # NEWCreate an division for adding dropdown helper text for report type
                                        html.Div(
                                            [
                                            html.H2('Select a Launch Site:', style={'margin-right': '2em'}),
                                            ]
                                        ),
                                        # NEW 
                                        dcc.Dropdown(id='site-dropdown', 
                   options=[
                           {'label': 'All Sites', 'value': 'OPT3'},
                           {'label': 'CCAFS LC-40', 'value': 'OPT4'},
                           {'label': 'CCAFS SLC-40', 'value': 'OPT5'},
                           {'label': 'KSC LC-39A', 'value': 'OPT6'},
                           {'label': 'VAFB SLC-4E', 'value': 'OPT7'}
                           ],
                  placeholder='Select a Launch Site',
                  value='OPT3',
                  searchable=True,
                  style={'width':'80%','padding':'3px', 'text-align-last': 'center', 'font-size': '20px'})
                                    # NEWPlace them next to each other using the division style
                                    ], style={'display':'flex'}),
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),






                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                   html.Div([
                                       # new
                                        html.Div(
                                            [
                                            html.H2('Payload Range (kg):', style={'margin-right': '2em'})
                                            ]
                                        ),
                                        dcc.RangeSlider(id='payload-slider', 
                                                     # new
                                                     min=0,
                                                     max=10000,
                                                     step=1000,marks={
        0: '0',
        2500: '2500',
        5000: '5000',
        7500: '7500',
        10000: '10000'
    },
                                                     value=[min_payload, max_payload]
                                                     #style={'width':'80%', 'padding':'3px', 'font-size': '20px', 'text-align-last' : 'center'}
                                                     ),
                                            # Place them next to each other using the division style
                                            ], #style={'display': 'flex'}
                                            ),  



                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# Add computation to callback function and return graph


#@app.callback(
#    Output(component_id='success-pie-chart', component_property='figure'),
#    Input(component_id='site-dropdown', component_property='value')
#)


#def generate_chart(names, values):


        #success-pie-chart = px.pie(spacex_df, values='class', names='Launch_Site', title='Successful Launches for All Sites')
        #return success-pie-chart





# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)