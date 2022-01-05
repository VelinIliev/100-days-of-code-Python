import pandas

data = pandas.read_csv("./squirrel_data.csv")

# fur_to_list = data["Primary Fur Color"]

# black = 0
# cinnamon = 0
# gray = 0
#
# for color in fur_to_list:
#     if color == "Black":
#         black += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#     elif color == "Gray":
#         gray += 1

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_squirrels_count, cinnamon_squirrels_count, grey_squirrels_count]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("./squirrels_count.csv")