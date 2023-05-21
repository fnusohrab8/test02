import requests

def main():
    # Prompt the user to enter a city or zip code
    location = input("Enter a city name or area code: ")
    
    # Use a try block to establish a connection to the OpenWeatherMap API
    try:
        api_key = "110214ffce59b1ceeb412d431a0b8ef4"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if there was an error with the request
    except requests.exceptions.HTTPError:
        print("Error: Invalid input or unable to connect to OpenWeatherMap API.")
        return
    
    # Convert the API response to a dictionary object
    data = response.json()
    
    # Extract the relevant weather data from the dictionary
    city = data["name"]
    temp = round(data["main"]["temp"] - 273.15, 1)  # Convert temperature from Kelvin to Celsius
    weather_desc = data["weather"][0]["description"]
    
    # Display the weather forecast to the user
    print(f"\nCurrent weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {weather_desc}")

if __name__ == "__main__":
    while True:
        main()
        response = input("\nWould you like to check another location? (Y/N) ").lower()
        if response != "y":
            break
