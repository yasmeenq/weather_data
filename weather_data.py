weather_data = {}

#allow user to input as many cities as needed + input temperature, humidity, wind-speed for each city
city = str(input("Enter city name or -99 to exit: ")).lower()
if city == "-99":
    print("exiting ")
else:
    while city != "-99":
        weather_data[city]={}

        temperature = float(input(f"Enter temperature in {city}: "))
        humidity = float(input(f"Enter humidity in {city}: "))
        wind_speed = float(input(f"Enter wind-speed in {city}: "))
        print()

        for city in weather_data:
            weather_data[city]["temperature"] = temperature
            weather_data[city]["humidity"] = humidity
            weather_data[city]["wind speed"] = wind_speed 
        city = input("Enter city name or -99 to exit: ").lower()
print(weather_data)
print()

# request: add remove and view data

request = str(input("type: add, remove, view or no to exit: ")).strip().lower()
print()

while request != "no":

    #add data
    if request == "add":
        ask = str(input("To add a new city, type city || To add weather data to a certain city, type data: ")).strip().lower()

        #add a new city to the main dictionary
        if ask == "city":
            city_name = str(input("city name: ")).lower()
            weather_data[city_name] = {}
        #ask for data to this city
            temperature = float(input(f"Enter temperature in {city_name}: "))
            humidity = float(input(f"Enter humidity in {city_name}: "))
            wind_speed = float(input(f"Enter wind-speed in {city_name}: "))
        #add the data to the city
            weather_data[city_name]["Temperature"] = temperature
            weather_data[city_name]["Humidity"] = humidity
            weather_data[city_name]["Wind Speed"] = wind_speed 
        #print the dictionary with the new city and its data added to it
            print(weather_data)
            print()

        #add new data to a certain city
        elif ask == "data":
            city = str(input("to what city you'd like to add data?")).strip().lower()
            if city in weather_data:
                data_name = str(input("Enter data name: ")).strip().lower()
                data_value = float(input("Enter data value: "))
                weather_data[city][data_name] = data_value
                print(weather_data)
                print()
            else:
                print("city not found")
    
    
    #remove data:
    if request == "remove":
        ask = str(input("To remove a city, type city || To remove weather data from a certain city, type data: ")).strip().lower()
        #remove a certain city completely 
        if ask == "city":
            city = str(input("input city name you want to remove: ")).strip().lower()
            if city in weather_data:
                del weather_data[city]
                print("removed!")
                print(weather_data)
                print()
            else:
                print("city not found")
                print()
        #remove data from a specific city
        if ask == "data":
            city = str(input("input city name you want to remove data from: ")).lower().strip()
            if city in weather_data:
                data_name = str(input("input data name you want to remove: ")).strip().lower()
                if data_name in weather_data[city]:
                    del weather_data[city][data_name]
                    print("removed!")    
                    print(weather_data)
                    print()    
            else:
                print("city not found")
                print()

    #view data for a certain city
    if request == "view":
        city = str(input("Enter city name you want to view its data: ")).lower().strip()           
        if city in weather_data:
            print(city, weather_data[city])
            print()
        else:
            print("city not found")
            print()


    request = str(input("type: add, remove, view or no to exit: ")).strip().lower()
        
print(weather_data)       
print("exiting program") 


