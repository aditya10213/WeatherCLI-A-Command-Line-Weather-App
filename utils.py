from colorama import Fore, Style
def format_weather(city, weather):
    return (
        Fore.CYAN + f"Weather for {city.capitalize()}:\n" + Style.RESET_ALL +
        f"Temperature: {weather['temperature']}°C\n"
        f"Windspeed : {weather['windspeed']} km/h\n"
    )
def format_weather(city, weather):
    return (
        f"Weather for {city.capitalize()}:\n"
        f"Temperature: {weather['temperature']}°C\n"
        f"Windspeed : {weather['windspeed']} km/h\n"
    )
