import requests

headers = {
    "User-Agent": "Student"
}
location_params = {
    "q": input("Input location: "),
    "format": "json",
    "limit": 1,
    "addressdetails": 1
}

location_url = 'https://nominatim.openstreetmap.org/search?'
location_response = requests.get(location_url, params = location_params, headers = headers)
if location_response.status_code != 200:
    print("Invalid Entry!")
    exit()

location_data = location_response.json()

lat = location_data[0]['lat']
lon = location_data[0]['lon']

weather_grid_url = "https://api.weather.gov/points/" + lat + "," + lon
weather_grid_response = requests.get(weather_grid_url, headers = headers)
weather_grid_data = weather_grid_response.json()

office = weather_grid_data['properties']['gridId']
gridX = weather_grid_data['properties']['gridX']
gridY = weather_grid_data['properties']['gridY']

weather_url = 'https://api.weather.gov/gridpoints/' + office + '/' + str(gridX) + ',' + str(gridY) + '/forecast'
weather_response = requests.get(weather_url, headers = headers)
weather = weather_response.json()

city = location_data[0]['address']['city']
state = location_data[0]['address']['state']
print(f"\n7 day forecast for {city}, {state}")

strlen = len(f"\n7 day forecast for {city}, {state}")
for i in range(strlen):
    print('-', end="")
print("\n")

print("WHEN".center(20) + '|' + "TEMP".center(15) + '|' + "PRECIPITATION".center(20) + '|' + "WIND".center(23) + '|')

strlen = len("WHEN".center(20) + '|' + "TEMP".center(15) + '|' + "PRECIPITATION".center(20) + '|' + "WIND".center(23) + '|')
for i in range(strlen):
    print('-', end="")
print("\n")

for i in weather['properties']['periods']:
    if i['number'] % 2 == 0:
        name = i['name']
        temperature = "Low of " + str(i['temperature']) + i['temperatureUnit']
        precipitation = str(i['probabilityOfPrecipitation']['value']) + "% chance of rain"
        wind = "Wind " + i['windSpeed'] + ' ' +  i['windDirection']

        print(f"{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|")
    else:
        name = i['name']
        temperature = "High of " + str(i['temperature']) + i['temperatureUnit']
        precipitation = str(i['probabilityOfPrecipitation']['value']) + "% chance of rain"
        wind = "Wind " + i['windSpeed'] + ' ' +  i['windDirection']

        print(f"{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|")

    strlen = len(f"{name:20s}| {temperature:14s}| {precipitation:19s}| {wind:22s}|")
    for i in range(strlen):
        print('-', end="")
    
    print("\n")