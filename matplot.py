import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Create an SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1/viral')

# Define your MySQL queries to retrieve data for Twitter and YouTube
query_twitter = "SELECT `Posts(in K)`, Topic FROM trend WHERE Plateform = 'Twitter'"
query_youtube = "SELECT `Posts(in K)`, Topic FROM trend WHERE Plateform = 'YouTube'"

# Retrieve data using pandas and SQLAlchemy
df_twitter = pd.read_sql_query(query_twitter, engine)
df_youtube = pd.read_sql_query(query_youtube, engine)

# Sort DataFrames by 'Topic' in ascending order
df_twitter = df_twitter.sort_values(by='Topic')
df_youtube = df_youtube.sort_values(by='Topic')

# Create interactive bar graphs using plotly
fig_twitter = px.bar(df_twitter, x='Topic', y='Posts(in K)', labels={'Posts(in K)': 'Posts (in K)'}, title='Twitter Bar Graph')
fig_youtube = px.bar(df_youtube, x='Topic', y='Posts(in K)', labels={'Posts(in K)': 'Posts (in K)'}, title='YouTube Bar Graph')

# Save the interactive plots as HTML files
fig_twitter.write_html('graph_twitter.html')
fig_youtube.write_html('graph_youtube.html')
