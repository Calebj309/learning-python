import requests

#Header required for GET requests
headers = {
    'User-Agent': 'weather app'
}

def get_location_params(user_input):
    location_params = {
        'q': user_input,
        'format': 'json',
        'limit': 1,
        'addressdetails': 1
    }
    location_baseurl = 'https://nominatim.openstreetmap.org/search?'
    location_response = requests.get(location_baseurl, params = location_params, headers = headers)

    return location_response

def get_forecast(user_input):

    location_response = get_location_params(user_input)
    location_data = location_response.json()
    
    #Making sure the location is in the US, getting new location if now
    while location_response.status_code != 200 or len(location_data) == 0 or location_data[0]['address']['country_code'] != 'us':
        location_response = get_location_params(input('Invalid entry! Please enter a location: '))
        location_data = location_response.json()
        
    #Storing lat, lon, city and state data
    lat = location_data[0]['lat']
    lon = location_data[0]['lon']
    city = location_data[0]['name']
    state = location_data[0]['address']['state']
  
    forecast_text = f'7 day forecast for {city}, {state}'

    print(f'\n{forecast_text:=^80}\n')

    #Gets the grid data used by the National Weather Service based on provided lat and lon data
    weather_grid_url = 'https://api.weather.gov/points/' + lat + ',' + lon
    weather_grid_response = requests.get(weather_grid_url, headers = headers)
    if weather_grid_response.status_code != 200:
        print('Invalid entry! Make sure your location was spelled correctly, or try entering a more populous location.')
        exit()
    weather_grid_data = weather_grid_response.json()

    #Stores office and grid data used by the National Weather Service
    office = weather_grid_data['properties']['gridId']
    gridX = weather_grid_data['properties']['gridX']
    gridY = weather_grid_data['properties']['gridY']

    #Uses office and grid data to grab forecast data from API
    weather_url = 'https://api.weather.gov/gridpoints/' + office + '/' + str(gridX) + ',' + str(gridY) + '/forecast'
    weather_response = requests.get(weather_url, headers = headers)
    weather = weather_response.json()

    ###Everything below handles printing the data###
    #Prints top label of graph
    print('WHEN'.center(20) + '|' + 'TEMP'.center(15) + '|' + 'PRECIPITATION'.center(20) + '|' + 'WIND'.center(23) + '|')

    #Makes line below graph label that is the length of the label
    strlen = len('WHEN'.center(20) + '|' + 'TEMP'.center(15) + '|' + 'PRECIPITATION'.center(20) + '|' + 'WIND'.center(23) + '|')
    for i in range(strlen):
        print('-', end="")
    print("\n", end="")

    #Prints all the data
    for i in weather['properties']['periods']:
        #Handles night temps, low temp provided
        if 'night' in i['name'].lower():
            name = i['name']
            temperature = 'Low of ' + str(i['temperature']) + i['temperatureUnit']
            precipitation = str(i['probabilityOfPrecipitation']['value']) + "% chance of rain"
            wind = 'Wind ' + i['windSpeed'] + ' ' +  i['windDirection']

            print(f'{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|')

        #Handles day temps, high temp provided
        else:
            name = i['name']
            temperature = 'High of ' + str(i['temperature']) + i['temperatureUnit']
            precipitation = str(i['probabilityOfPrecipitation']['value']) + '% chance of rain'
            wind = 'Wind ' + i['windSpeed'] + ' ' +  i['windDirection']

            print(f'{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|')

        #Prints line below each row that is the length of the row
        strlen = len(f'{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|')
        for i in range(strlen):
            print('-', end="")
        print("\n", end="")


introtext = "Welcome to Caleb's Weather Service!"
print(f'{introtext:=^80}\n')

while True:
    user_input = input('Enter a location in the United States to receive a weather forecast: ')
    if user_input.lower() in {'quit', 'q', 'end', 'close', 'stop'}:
        break
    get_forecast(user_input)