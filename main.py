# Create a Python Application which asks the user for their zip code or city
# Use the zip code or city name in order to obtain weather forecast data from http://openweathermap.org
# Display the weather forecast in a readable format to the user
# Use comments within the application, where appropriate, in order to document what the program is doing
# Use functions including a main function
# Allow the user to run the program multiple times
# Validate whether the user entered valid data. If valid data isn't presented notify the user
# Use the Requests library in order to request data from teh webservice
# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

import classes as c
import functions as f
    
def main():
    '''Main function'''
    program_running = True
    while program_running:
        location = input("Welcome. Please provide the city name or the zipcode for the location's weather: ")
        # checks if input is a valid zip code first
        if f.is_zip_code(location):
            # only pull first five digits of zip for query
            location = location[:5]
            weather = c.ZipCodeLocationWeather(location)
        # if not zip check if valid input for city name
        elif f.is_valid_city_name(location):
            state = input("Please provide the city's state: ")
            state = f.check_usa_state(state)
            weather = c.CityLocationWeather(location, state)

        else:
            print('Location selected is not a valid zipcode or city. Please try again.')
            program_running = f.go_again()
            continue
        
        weather.display_weather()
        program_running = f.go_again()    

    print('Thank you for using the program. Goodbye.')

# call main function
main()