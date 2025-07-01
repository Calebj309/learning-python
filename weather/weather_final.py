import requests

WHEN_WIDTH = 20
TEMP_WIDTH = 15
PRECIP_WIDTH = 20
WIND_WIDTH = 23
GRAPH_WIDTH = 83
headers = {
    "User-agent": "weather app"
}

def get_input():
    invalid = True
    user_input = input()
    while invalid == True:
        if has_numbers(user_input) or user_input == 'us':
            user_input = input("Invalid entry! Please enter a valid location: ")
        elif user_input == {'quit', 'q', 'end', 'close', 'stop'}:
            quit_check(user_input)
        else:
            invalid = False
    return user_input


def has_numbers(user_input):
    if any(char.isdigit() for char in user_input):
        return True
    else:
        return False
    

def get_location(user_input):
    location_params = {
        'q': user_input,
        'format': 'json',
        'limit': 1,
        'addressdetails': 1
    }
    location_baseurl = 'https://nominatim.openstreetmap.org/search?'
    location_response = requests.get(location_baseurl, params = location_params, headers = headers)

    return location_response


def get_weather_data(user_input):

    location_response = get_location(user_input)
    location_data = location_response.json()

    while location_response.status_code != 200 or len(location_data) == 0 or location_data[0]['address']['country_code'] != 'us':
        print("Invalid entry! Please enter a valid location: ", end='')
        user_input = get_input()
        quit_check(user_input)
        location_response = get_location(user_input)
        location_data = location_response.json()

    lat = location_data[0]['lat']
    lon = location_data[0]['lon']
    city = location_data[0]['address'].get('locality') or location_data[0]['address'].get('village') or location_data[0]['address'].get('town') or location_data[0]['address'].get('city')
    state = location_data[0]['address']['state']
  
    if city == None:
        forecast_text = f' 7 day forecast for {state} '
    else:
        forecast_text = f' 7 day forecast for {city}, {state} '

    print(f'\n{forecast_text:=^{GRAPH_WIDTH}}\n')

    weather_grid_url = 'https://api.weather.gov/points/' + lat + ',' + lon
    weather_grid_response = requests.get(weather_grid_url, headers = headers)
    weather_grid_data = weather_grid_response.json()

    office = weather_grid_data['properties']['gridId']
    gridX = weather_grid_data['properties']['gridX']
    gridY = weather_grid_data['properties']['gridY']

    weather_url = 'https://api.weather.gov/gridpoints/' + office + '/' + str(gridX) + ',' + str(gridY) + '/forecast'
    weather_response = requests.get(weather_url, headers = headers)
    weather = weather_response.json()

    return weather
    

def print_header(WHEN_WIDTH, TEMP_WIDTH, PRECIP_WIDTH, WIND_WIDTH):

    print(f'|{'WHEN'.center(WHEN_WIDTH)}|{'TEMP'.center(TEMP_WIDTH)}|{'PRECIPITATION'.center(PRECIP_WIDTH)}|{'WIND'.center(WIND_WIDTH)}|')

    strlen = len(f'|{'WHEN'.center(WHEN_WIDTH)}|{'TEMP'.center(TEMP_WIDTH)}|{'PRECIPITATION'.center(PRECIP_WIDTH)}|{'WIND'.center(WIND_WIDTH)}|')
    for i in range(strlen):
        print('-', end="")
    print("\n", end="")

    
def print_weather(weather, WHEN_WIDTH, TEMP_WIDTH, PRECIP_WIDTH, WIND_WIDTH):
    for i in weather['properties']['periods']:
        if 'night' in i['name'].lower():
            name = i['name']
            temperature = 'Low of ' + str(i['temperature']) + i['temperatureUnit']
            precipitation = str(i['probabilityOfPrecipitation']['value']) + "% chance of rain"
            wind = 'Wind ' + i['windSpeed'] + ' ' +  i['windDirection']

            print(f'| {name:<{WHEN_WIDTH - 1}}| {temperature:<{TEMP_WIDTH - 1}}| {precipitation:<{PRECIP_WIDTH - 1}}| {wind:<{WIND_WIDTH - 1}}|')

        else:
            name = i['name']
            temperature = 'High of ' + str(i['temperature']) + i['temperatureUnit']
            precipitation = str(i['probabilityOfPrecipitation']['value']) + '% chance of rain'
            wind = 'Wind ' + i['windSpeed'] + ' ' +  i['windDirection']

            print(f'| {name:<{WHEN_WIDTH - 1}}| {temperature:<{TEMP_WIDTH - 1}}| {precipitation:<{PRECIP_WIDTH - 1}}| {wind:<{WIND_WIDTH - 1}}|')

        strlen = len(f'| {name:<{WHEN_WIDTH - 1}}| {temperature:<{TEMP_WIDTH - 1}}| {precipitation:<{PRECIP_WIDTH - 1}}| {wind:<{WIND_WIDTH - 1}}|')
        for i in range(strlen):
            print('-', end="")
        print("\n", end="")


def master_data_print(weather):

    print_header(WHEN_WIDTH, TEMP_WIDTH, PRECIP_WIDTH, WIND_WIDTH)
    print_weather(weather, WHEN_WIDTH, TEMP_WIDTH, PRECIP_WIDTH, WIND_WIDTH)

    print('Enter another location, or type "quit" to quit: ', end='')


def quit_check(user_input):
    if user_input.lower() in {'quit', 'q', 'end', 'close', 'stop'}:
        print('Exiting...')
        exit()    


introtext = "Welcome to Caleb's Weather Service!"
print(f'{introtext:=^{GRAPH_WIDTH}}\n')
print('Enter a location in the United States to receive a weather forecast, or type "quit" to quit: ')

while True:
    user_input = get_input()
    quit_check(user_input)
    weather = get_weather_data(user_input)
    master_data_print(weather)