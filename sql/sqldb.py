
import pandas as pd
import sqlite3

# Load the CSV file
csv_file_path = '/home/nevo/Downloads/weatherdb/1. Weather Data.csv'
df = pd.read_csv(csv_file_path)

# Create a SQLite database and connect to it
conn = sqlite3.connect('weather_data.db')

# Write the dataframe to a SQL table
df.to_sql('weather_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

