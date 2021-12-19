def calculator (first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number


first_number = float(input("What is the first number? "))
print("+\n-\n*\n/")

operation = input("Select operation ")
second_number = float(input("What is the next number? "))

result = calculator(first_number = first_number, operation = operation, second_number = second_number)
print(result)
continue_calc = input("Type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation: ")