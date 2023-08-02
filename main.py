# Create a Python Application which asks the user for their zip code or city
# Use the zip code or city name in order to obtain weather forecast data from http://openweathermap.org
# Display the weather forecast in a readable format to the user
# Use comments within the application, where appropriate, in order to document what the program is doing
# Use functions including a main function
# Allow the user to run the program multiple times
# Validate whether the user entered valid data. If valid data isn't presented notify the user
# Use the Requests library in order to request data from teh webservice
# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful

import json, requests

class LocationWeather():
    '''Parent class LocationWeather'''
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.appid = "039cf388d6d9f7b3d3aa4207a4a92d7e"
        self.url = None
        self.temp = None
        self.temp_max = None
        self.forecast = None

    def get_response_json(self):
        '''Sends request for response json'''
        try:
            response = requests.get(self.url)
            unformatted_data = response.json()
        except Exception:
            return None
        else:
            return unformatted_data

    def get_temp(self):
        '''Returns temp'''
        return self.temp
    def set_temp(self, temp):
        '''Sets temp'''
        self.temp = temp
    def get_temp_max(self):
        '''Returns temp_max'''
        return self.temp_max
    def set_temp_max(self, temp_max):
        '''Sets temp_max'''
        self.temp_max = temp_max
    def get_forecast(self):
        '''Return forecast'''
        return self.forecast
    def set_forecast(self, forecast):
        '''Sets forecast'''
        self.forecast = forecast

    def set_weather_attributes(self, weather_json):
        '''This pulls the info from the json response and sets values to attributes'''
        self.set_temp(weather_json['main']['temp'])
        self.set_temp_max(weather_json['main']['temp_max'])
        self.set_forecast(weather_json['weather'][0]['main'])

    def display_weather(self):
        '''This calls the get_response_json and formatted/displays json data.'''
        json_data = self.get_response_json()
        if json_data is None:
            print('Sorry, there was an error with retrieving weather. Please try again.')
        else:
            self.set_weather_attributes(json_data)     
            print(f'The current temperature is {self.get_temp()}.')
            print(f'The max temperature is {self.get_temp_max()}.')
            print(f'The forcast is {self.get_forecast()}.')

class ZipCodeLocationWeather(LocationWeather):
    '''Weather location by zip code, child of LocationWeather'''
    def __init__(self, zipcode):
        super().__init__()
        self.zipcode = zipcode
        self.url = f'{self.base_url}?q={self.zipcode},us&units=imperial&APPID={self.appid}'

class CityLocationWeather(LocationWeather):
    '''Weather location by city, child of LocationWeather'''
    def __init__(self, city, state):
        super().__init__()
        self.city = city
        self.state = state
        self.url = f'{self.base_url}?q={self.city},{self.state},us&units=imperial&APPID={self.appid}'
    
def isZipCode(zipcode):
    '''Checks to see if input is a zipcode. Returns True/False'''
    zip_check = zipcode.replace(' ', '')
    zip_check = zip_check.replace('-', '')
    if len(zip_check) != 5 and len(zip_check) != 9:
        return False
    for i in range(len(zip_check)):
        if zip_check[i].isalpha():
            return False
    return True

def goAgain():
    '''Asks user if they wish to go again or quit'''
    keep_going = input('Do you want to go search again? (y/n) ')
    if keep_going.lower() == 'y' or keep_going.lower() == 'yes':
        return True
    elif keep_going.lower() == 'n' or keep_going.lower() == 'no':
        return False
    else:
        goAgain()

def main():
    '''Main function'''
    program_running = True
    while program_running:
        location = input("Welcome. Please provide the city name or the zipcode for the location's weather: ")
        if isZipCode(location):
            weather = ZipCodeLocationWeather(location)
        else:
            state = input("Please provide the city's state: ")
            weather = CityLocationWeather(location, state)

        weather.display_weather()
        program_running = goAgain()    

    print('Thank you for using the program. Goodbye.')
main()