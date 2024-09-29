import gspread
import pandas as pd

from sqlalchemy import create_engine


import mysql.connector

# Authenticate with Google Sheets
gc = gspread.service_account(filename=r"C:\Users\kachh\Downloads\viral-wave-82ab6286db42.json")

# Open the Google Sheets document
worksheet = gc.open_by_key("1gqXKu5i6tLaKKaEKZW-E4O7dQ4HUVo5iaReW6I_54sM")
current_sheet = worksheet.sheet1

# Get all values from the sheet
data = current_sheet.get_all_values()
print(data)  # Print the data to verify

df = pd.DataFrame(data[1:], columns=data[0])

# MySQL connection settings
db_user = 'root'
db_password = '1234'
db_host = '127.0.0.1'
db_port = '3306'
db_name = 'viral'
table_name = 'trend'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
# Create a MySQL connection
conn = mysql.connector.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

# Create a SQLAlchemy engine using mysql-connector-python
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Write the DataFrame to the MySQL database
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the MySQL connection
conn.close()