import random
from datetime import datetime, timedelta


def generate_weather_data(start_date, end_date):
    """Generate random weather data between start_date and end_date."""
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)

    delta = end - start
    weather_data = []

    for i in range(delta.days + 1):
        current_date = start + timedelta(days=i)
        date_str = current_date.strftime(date_format)

        max_temp = random.randint(
            20, 35
        )  # Random max temperature between 20°C and 35°C
        min_temp = random.randint(
            15, max_temp
        )  # Random min temperature between 15°C and max_temp
        humidity = random.randint(40, 80)  # Random humidity between 40% and 80%

        weather_data.append(
            {
                "date": date_str,
                "max_temp": max_temp,
                "min_temp": min_temp,
                "humidity": humidity,
            }
        )

    return weather_data


# Generate data from August 1, 2023 to July 10, 2024
start_date = "2023-08-01"
end_date = "2024-07-10"
weather_data = generate_weather_data(start_date, end_date)
