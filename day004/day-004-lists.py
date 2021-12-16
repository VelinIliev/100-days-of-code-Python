fruits = ["banana", "orange", "pear"]
# states = ["Ohaio", "Pennsylvania", "Texas"] 

fruits[0] = "apple"

fruits.append("ananas")

print(fruits[0])
print(fruits[-1])

fruits.extend(["strawberries", "peach"])

print(fruits)
print(len(fruits))

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",
# "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"] 
fruitsd = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruitsd, vegetables]
print(dirty_dozen)