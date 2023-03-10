import os
import requests
from pprint import pprint


class WeatherSnatcher:
    def __init__(self):
        # GET api key from environment variable
        self.my_secret = os.environ['apikey']
        self.location = None
        self.c_or_f = None
        self.response = None

    # Ask user for location
    def define_validate_input(self):
        while True:
            # Get location data from user
            self.location = input("What is your current location? (City, State OR Zip Code): ")
            # Get celcius or fahrenheit
            self.c_or_f = input("Celcius of Fahrenheit? (C or F): ")
            # Make request to weather API
            self.api_url = f'http://api.weatherapi.com/v1/current.json?key={self.my_secret}&q={self.location}&aqi=no'
            self.response = requests.get(self.api_url)
            # Check if location is valid
            if self.response.status_code == 200:
                break
            else:
                print("Invalid location. Please try again.")
                
    # GET weather
    def get_weather(self):
        # check if the api call is valid or not and return current temp in Celcius
        if self.response.status_code == 200 and self.c_or_f == "C":
            pprint('The current temperature outside is: ' + self.response.json()["current"]['temp_c'])
        # check if the api call is valid or not and return current temp in Farhenhiet
        elif self.response.status_code == 200 and self.c_or_f == "F":
            pprint('The current temperature outside is: ' + self.response.json()["current"]['temp_f'])
        else:
            print(f'Request failed with status code {self.response.status_code}')


weather = WeatherSnatcher()
weather.define_validate_input()
weather.get_weather()
del weather