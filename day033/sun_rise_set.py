import requests

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
# 42.687, 23.36
# date(string) YYYY-MM-DD
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2021-12-16

URL = "https://api.sunrise-sunset.org/json?"
LATITUDE = 42.6940052
LONGITUDE = 23.3531573
BG_TIME = 2

def convert_to_24H(hour_to_convert):
    temp = hour_to_convert.split(" ")
    time = temp[0].split(":")
        
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    if temp[1] == "PM":
        hours = hours + 12 + BG_TIME
    elif temp[1] == "AM":
        hours = hours + BG_TIME
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def convert_to_seconds(hour_to_convert):
    temp = hour_to_convert.split(" ")
    time = temp[0].split(":")
    hours = int(time[0])*3600
    minutes = int(time[1])*60
    seconds = int(time[2])
    return hours + minutes + seconds

all_data = []

for day in range(2,21):
    if day < 10:
        date = f'2022-01-0{day}'
    else: 
        date = f'2022-01-{day}'

    response = requests.get(url=f'{URL}lat={LATITUDE}&lng={LONGITUDE}&date={date}')
    response.raise_for_status()

    data = response.json()["results"]
    
    sunrise = data["sunrise"]
    sunset = data["sunset"]
    daylength = data["day_length"]
    new_element = {
        "date": date, 
        "sunrise": sunrise,
        "sunset":sunset,
        "daylight":daylength}

    all_data.append(new_element)

    if len(all_data)>1:
        today = convert_to_seconds(all_data[-1]['daylight'])
        yestarday = convert_to_seconds(all_data[-2]['daylight'])
        difrence_with_yestarday = f'{today - yestarday} сек'
    else:
        difrence_with_yestarday = ""

    with open("./sun.txt", mode = "a") as file:
        file.write(f"дата: {date} | изгрев: {convert_to_24H(sunrise)} | залез: {convert_to_24H(sunset)} | продължителност на деня: {daylength} | разлика: {difrence_with_yestarday}\n")

# print(convert_to_seconds(all_data[-1]['daylight'])-convert_to_seconds(all_data[0]['daylight']))