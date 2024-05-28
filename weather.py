
import requests

def fetch_weather(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        print(f"Location: {city}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
    else:
        print("Error: Unable to fetch weather data.")

def main():
    api_key = '00dc4255d19f0fa8b2b5e7ba47bf2766'  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
