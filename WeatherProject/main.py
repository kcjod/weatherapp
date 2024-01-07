import requests
import json

try:
    city = input("Enter the name of city:")

    data = requests.get(f"API_KEY={city}")
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
