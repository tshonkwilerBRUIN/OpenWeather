# File contains the class LocationWeather
# and children ZipCodeLocationWeather
# and CityLocationWeather
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
        self.humidity = None
        self.temp_min = None

    def get_response_json(self):
        '''Sends request for response json'''
        try:
            response = requests.get(self.url)
            if response.status_code == 404:
                return 'Not Found'
            elif response.status_code >= 300:
                raise Exception
            else:
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
        '''Returns forecast'''
        return self.forecast
    def set_forecast(self, forecast):
        '''Sets forecast'''
        self.forecast = forecast
    def get_humidity(self):
        '''Returns humidity'''
        return self.humidity
    def set_humidity(self, humidity):
        '''Sets humidity'''
        self.humidity = humidity
    def get_temp_min(self):
        '''Returns temp_min'''
        return self.temp_min
    def set_temp_min(self, temp_min):
        '''Sets temp_min'''
        self.temp_min = temp_min

    def set_weather_attributes(self, weather_json):
        '''This pulls the info from the json response and sets values to attributes'''
        self.set_temp(weather_json['main']['temp'])
        self.set_temp_max(weather_json['main']['temp_max'])
        self.set_forecast(weather_json['weather'][0]['main'])
        self.set_humidity(weather_json['main']['humidity'])
        self.set_temp_min(weather_json['main']['temp_min'])

    def display_weather(self):
        '''This calls the get_response_json and formatted/displays json data.'''
        json_data = self.get_response_json()
        if json_data == 'Not Found':
            print('Request to OpenWeatherMap was not successful.')
            print('Requested location was not found. Please check input and try again.')
        elif json_data is None:
            print('Request to OpenWeatherMap was not successful.')
            print('Sorry, there was an error with retrieving weather. Please try again.')
        else:
            print('Request to OpenWeatherMap was successful.')
            print()
            self.set_weather_attributes(json_data)     
            print(f'The current temperature is {self.get_temp()}.')
            print(f'The max temperature is {self.get_temp_max()}.')
            print(f'The min temperature is {self.get_temp_min()}')
            print(f'The forcast is {self.get_forecast()}.')
            print(f'The humidity is {self.get_humidity()}%.')
            print()

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
        # will utilize state in url if not blank
        if self.state == '':
            self.url = f'{self.base_url}?q={self.city}&units=imperial&APPID={self.appid}'
        else:
            self.url = f'{self.base_url}?q={self.city},{self.state},us&units=imperial&APPID={self.appid}'