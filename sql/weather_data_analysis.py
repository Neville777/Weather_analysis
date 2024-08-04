import pandas as pd
import sqlite3
import numpy as np

# Connect to the database
conn = sqlite3.connect('weather_data.db')

# Question 1: Find all records where the weather was exactly clear.
print("Records where the weather was exactly clear:")
clear_weather = pd.read_sql_query("SELECT * FROM weather_data WHERE Weather = 'Clear'", conn)
print(f"Number of clear weather records: {len(clear_weather)}")

# Question 2: Find the number of times the wind speed was exactly 4 km/hr.
wind_speed_4_kmph = pd.read_sql_query("SELECT COUNT(*) as count FROM weather_data WHERE \"Wind Speed_km/h\" = 4", conn)
print(f"\nNumber of times the wind speed was exactly 4 km/hr: {wind_speed_4_kmph['count'].values[0]}")

# Question 5: What is the mean visibility of the dataset?
visibility_data = pd.read_sql_query("SELECT Visibility_km FROM weather_data", conn)
mean_visibility = np.mean(visibility_data['Visibility_km'])
print(f"\nMean visibility of the dataset: {mean_visibility} km")

# Question 9: Find the number of weather conditions that include snow.
snow_conditions = pd.read_sql_query("SELECT COUNT(*) as count FROM weather_data WHERE Weather LIKE '%Snow%'", conn)
print(f"\nNumber of weather conditions that include snow: {snow_conditions['count'].values[0]}")

# Additional analysis using NumPy
visibility_array = np.array(visibility_data['Visibility_km'])
print(f"\nStandard deviation of visibility: {np.std(visibility_array)} km")
print(f"Median visibility: {np.median(visibility_array)} km")
print(f"Maximum visibility: {np.max(visibility_array)} km")
print(f"Minimum visibility: {np.min(visibility_array)} km")

# Close the connection
conn.close()