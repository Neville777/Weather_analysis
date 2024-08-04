import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
csv_file_path = '/home/nevo/Downloads/weatherdb/1. Weather Data.csv'
df = pd.read_csv(csv_file_path)

# 1. Find all records where the weather was exactly clear.
clear_weather = df[df['Weather'] == 'Clear']
print("Records where the weather was exactly clear:")
print(clear_weather)

# 2. Find the number of times the wind speed was exactly 4 km/hr.
wind_speed_4_kmph = df[df['Wind Speed_km/h'] == 4].shape[0]
print(f"\nNumber of times the wind speed was exactly 4 km/hr: {wind_speed_4_kmph}")

# 3. Check if there are any NULL values present in the dataset.
null_values = df.isnull().sum()
print("\nCheck for NULL values in the dataset:")
print(null_values)

# 4. Rename the column "Weather" to "Weather_Condition."
df.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)
print("\nColumns after renaming:")
print(df.columns)

# 5. What is the mean visibility of the dataset?
mean_visibility = df['Visibility_km'].mean()
print(f"\nMean visibility of the dataset: {mean_visibility} km")

# 6. Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km.
specific_condition = df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)].shape[0]
print(f"\nNumber of records with wind speed > 24 km/hr and visibility_km = 25 km: {specific_condition}")

# 7. What is the mean value of each column for each weather condition?
# Convert 'Date/Time' to datetime and exclude it from mean calculation
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
numeric_columns = df.select_dtypes(include=[np.number]).columns
mean_values_per_weather = df.groupby('Weather_Condition')[numeric_columns].mean()
print("\nMean value of each column for each weather condition:")
print(mean_values_per_weather)

# 8. Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.
specific_conditions = df[(df['Weather_Condition'] == 'Clear') & ((df['Rel Hum_%'] > 50) | (df['Visibility_km'] > 40))]
print("\nInstances where the weather is clear and relative humidity > 50, or visibility > 40:")
print(specific_conditions)

# 9. Find the number of weather conditions that include snow.
snow_conditions = df[df['Weather_Condition'].str.contains('Snow', case=False, na=False)].shape[0]
print(f"\nNumber of weather conditions that include snow: {snow_conditions}")