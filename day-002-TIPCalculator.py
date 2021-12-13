print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
percentage = int(input("What precentage tip would you like to give? 10, 12 or 15?\n"))
peoples = int(input("How many people to split the bill?\n"))

total_bill = bill + bill*(percentage/100)
per_person = round(total_bill / peoples,2)

print(f'Total bill: {total_bill:.2f}$')
print(f'Each preson should pay: {per_person:.2f}$')