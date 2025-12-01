def format_weather(city, weather):
    return (
        f"Weather for {city.capitalize()}:\n"
        f"Temperature: {weather['temperature']}°C\n"
        f"Windspeed : {weather['windspeed']} km/h\n"
    )
