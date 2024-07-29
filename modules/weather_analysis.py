# weather_analysis.py

from .weather_data import weather_data


def highest_and_lowest_temps(data):
    """Find the highest and lowest temperatures recorded during the period."""
    max_temp = float("-inf")
    min_temp = float("inf")

    for entry in data:
        if entry["max_temp"] > max_temp:
            max_temp = entry["max_temp"]
        if entry["min_temp"] < min_temp:
            min_temp = entry["min_temp"]

    return max_temp, min_temp


def days_above_30(data):
    """Determine the number of days with temperatures above 30°C."""
    count = 0
    for entry in data:
        if entry["max_temp"] > 30:
            count += 1
    return count


def average_humidity(data):
    """Compute the average humidity over the specified period."""
    total_humidity = 0
    num_entries = len(data)

    for entry in data:
        total_humidity += entry["humidity"]

    return total_humidity / num_entries if num_entries > 0 else 0
