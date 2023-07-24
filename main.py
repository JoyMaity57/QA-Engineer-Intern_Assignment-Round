import requests


def get_weather(date):
    response = requests.get(
        "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    data_list = data["list"]
    temp = []
    for data in data_list:
        if date in data["dt_txt"]:
            temp.append(data["main"]["temp"])
    return temp


def get_wind_speed(date):
    response = requests.get(
        "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    data_list = data["list"]
    wind_speed = []
    for data in data_list:
        if date in data["dt_txt"]:
            wind_speed.append(data["wind"]["speed"])
    return wind_speed


def get_pressure(date):
    response = requests.get(
        "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    data_list = data["list"]
    pressure = []
    for data in data_list:
        if date in data["dt_txt"]:
            pressure.append(data["main"]["pressure"])
    return pressure


while True:
    print("Options:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        date = input("Enter the date: ")
        temperature = get_weather(date)
        print(f"The temperature on {date} is {temperature}°C.\n")
    elif option == 2:
        date = input("Enter the date: ")
        wind_speed = get_wind_speed(date)
        print(f"The wind speed on {date} is {wind_speed} km/h.\n")
    elif option == 3:
        date = input("Enter the date: ")
        pressure = get_pressure(date)
        print(f"The pressure on {date} is {pressure} hPa.\n")
    elif option == 0:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.\n")
