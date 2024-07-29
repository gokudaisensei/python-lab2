from modules.weather_analysis import (
    highest_and_lowest_temps,
    days_above_30,
    average_humidity,
)
from modules.weather_data import weather_data

# Find highest and lowest temperatures
max_temp, min_temp = highest_and_lowest_temps(weather_data)
print(f"Highest Temperature: {max_temp}°C")
print(f"Lowest Temperature: {min_temp}°C")

# Determine the number of days with temperatures above 30°C
num_days_above_30 = days_above_30(weather_data)
print(f"Number of Days with Temperature Above 30°C: {num_days_above_30}")

# Compute the average humidity
avg_humidity = average_humidity(weather_data)
print(f"Average Humidity: {avg_humidity:.2f}%")
