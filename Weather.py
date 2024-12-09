def display_welcome():
    print("Welcome to the weather app!")

def get_weather(city, weather_data):
    if city in weather_data:
        weather = weather_data[city]
        print(" Weather forecast for " + city + ": ")
        print(" Temperature: " + weather['temperature'])
        print(" Conditions: " + weather['conditions'])
        print(" Wind Speed: " + weather['wind_speed'])
        print(" Humidity: " + weather['humidity'])

def main():
    weather_data = {
        "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
        "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
        "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
        "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
        "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"}
    }

    display_welcome()


    try:
        city = input("Enter the city you'd like to view weather for: ")
        if city not in weather_data:
            raise ValueError(city, " could not be found in the weather data. Please try again!")
        else:
            get_weather(city, weather_data)
            pass
    except ValueError as x:
        print("error", x)
        main()


if __name__ == "__main__":
    main()

print("Thanks for using the app!")