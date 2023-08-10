# Contains the functions used in main.py

import csv
    
def is_zip_code(zipcode):
    '''Checks to see if input is a zipcode. Returns True/False'''
    zip_check = zipcode.replace(' ', '')
    zip_check = zip_check.replace('-', '')
    if len(zip_check) != 5 and len(zip_check) != 9:
        return False
    for i in range(len(zip_check)):
        if zip_check[i].isalpha():
            return False
    return True

def go_again():
    '''Asks user if they wish to go again or quit'''
    keep_going = input('Do you want to search again? (y/n) ')
    if keep_going.lower() == 'y' or keep_going.lower() == 'yes':
        return True
    elif keep_going.lower() == 'n' or keep_going.lower() == 'no':
        return False
    else:
        go_again()

def is_valid_city_name(city_name):
    '''Checks to see if the city name provided is valid.'''
    # city name must not contain numeric characters
    for character in city_name:
        if character.isdigit():
            return False
    # city name must have at least one character
    if len(city_name) == 0:
        return False

    return True

def check_usa_state(state_name):
    '''Checks if state provided is valid USA state or abbreviation.'''
    if state_name.title().strip() in usa_state_names() or state_name.upper().strip() in usa_state_abbreviations():
        return state_name.strip()
    else:
        return ''      

def usa_state_names():
    '''Returns tuple of USA state names'''
    try:
        with open('state_names.txt') as f:
            reader = csv.reader(f, delimiter=',')
            state_names = list(reader)
    except Exception:
        state_names = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 
                       'Connecticut','Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
                       'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
                       'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                       'Mississippi', 'Missouri', 'Montana', 'Nebraska','Nevada',
                       'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 
                       'North Carolina','North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 
                       'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
                       'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                       'West Virginia', 'Wisconsin', 'Wyoming')
        return state_names
    else:
        return tuple(state_names[0])

def usa_state_abbreviations():
    '''Returns tupe of USA state abbreviations'''
    try:     
        with open('state_abbreviations.txt') as f:
         reader = csv.reader(f, delimiter=',')
        state_abbreviations = list(reader)
    except Exception:
        state_abbreviations = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                               'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                               'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                               'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                               'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')
        return state_abbreviations
    else:
        return tuple(state_abbreviations[0])