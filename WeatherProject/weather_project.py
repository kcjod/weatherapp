import requests
import json

# My API Key - https://api.weatherapi.com/v1/current.json?key=371eca43fc074d089db143400232812&q=bulk
try:
    city = input("Enter the name of city:")

    data = requests.get(f"https://api.weatherapi.com/v1/current.json?key=371eca43fc074d089db143400232812&q={city}")
    # gives in nthe form of response (<class 'requests.models.Response'>)

    weather_info = data.text # converting data to string
    city_info = json.loads(weather_info) # convert string to dict

    print("Name :",city_info["location"]["name"])
    print("Country :",city_info["location"]["country"])
    print("Temperature :",city_info["current"]["temp_c"],"°C")

except:
    print("Enter a vaild location")

finally:
    print("Thank You for using our application")