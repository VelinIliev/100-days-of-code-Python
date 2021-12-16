import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

# random_index = random.randint(0, len(names)-1)
# print(f'{names[random_index]} will pay the bill!')

print(f'{random.choice(names)} will pay the bill!')
