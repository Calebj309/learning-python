This is a program I made that provides a 7 day forecast for a given location in the United States

It uses 2 APIs:
1. "https://nominatim.openstreetmap.org/" provides coordinate data for an entered location.
2. "https://api.weather.gov/", via multiple queries, gives the requested weather data based off of the coordinates Nominatim provides.

The folder contains all iterations of the project as I worked on it, with the final version being weather_final.py.

To run the program:
1. Make sure you have Python and the "Requests" library installed.
2. Open CMD and navigate to the directory weather_final.py is located.
   Alternatively, right click the white space of File Explorer while in the "weather" directory and click "Open in Terminal"
3. Type "py .\weather_final.py" and press enter
4. You'll now be greeted with the start screen of the weather program. Here you can enter a location, or type quit to quit.

Pointers for entering a location:
1. Keep your search broad. Rather than a specific address (eg. 123 park place, New York City, New York), enter "New York City", "nyc", etc.
2. Abbreviations for many locations will work, though if the abbreviation is not unique you may not get data for the desired location.
   For example, entering "um" provides forecast data for the University of Miami in Coral Gables, Florida, rather than data for the University of Michigan or Minnesota.
   Try alternate abbreviations if the expected location isn't being provided. For example, while "um" doesn't provide data for the University of Minnesota, "umn" does.
   You can also provide airport codes
3. The program accepts entries such as "Smithsonian Museum" or "Disneyland", which will provide data for Washington D.C. or Anaheim, California    respectively.
   Make sure your entry is specific enough to pick up the right location, or any location at all. Entering "science museum" won't provide any data. However, entering "science and nature museum" will provide data for Denver, home of the Museum of Nature and Science.
5. The state can be specified with or without a comma, and even with the state abbreviation.
   Providing just "springfield" will always give data for Springfield, Illinois. Appending "texas" or "tx", with or without a comma seperating the state, will provide data for Springfield, Texas.
6. You may enter just a state, but the forecast data will likely not be accurate to your location. It will provide data for the geographic center of the state you specify.
7. Strange inputs can unexpectedly yield data. For example, typing "googoo" gives you the forecast for Columbus, Georgia. because the Nominatim thinks you're searching for the GooGoo Express Car Wash in that city.

Known issues:
1. None. The code is perfect. Don't tell me if you find any, it will break me

Special thanks to Shelby and Jamie for assisting