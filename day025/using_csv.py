# import csv

# with open("./weather_data.csv") as file:
#     raw_data = file.readlines()
    
#     data = []
#     for line in raw_data:
#         new_line = line.replace('\n', "")
#         data.append(new_line)

# print(data)

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_to_list = data["temp"].to_list()
# print(temp_to_list)

# average = sum(temp_to_list) / len(temp_to_list)
# print(average)

# average = data["temp"].mean()
# print(average)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data.condition)
print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

monday_f = monday.temp*1.8+32
print(monday.temp, monday_f)