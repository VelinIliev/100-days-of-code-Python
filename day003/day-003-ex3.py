print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, ot L \n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y ot N\n")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoniS_price = 2
pepperoniML_price = 3
extra_cheese_price = 1

bill = 0

if size == "S" or size == "M" or size == "L":
    if size == "S":
        bill += small_pizza_price
    elif size == "M":
        bill += medium_pizza_price
    elif size == "L":
        bill += large_pizza_price

    if add_pepperoni == "Y":
        if size == "S":
            bill += pepperoniS_price
        elif size == "M" or size == "L": 
            bill += pepperoniML_price

    if extra_cheese == "Y":
        bill += extra_cheese_price

    print(f"Total price is: ${bill:.2f}")
else: 
    print("Please choose a size")