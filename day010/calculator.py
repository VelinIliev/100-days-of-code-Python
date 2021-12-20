def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiplay(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
    
operations = {
    "+": add,
    "-": substract,
    "*": multiplay,
    "/": divide,
}
end_of_calculation = False
start_position = 'yes'

while not end_of_calculation:
    if start_position == "yes":
        num1 = float(input("What is the first number? "))
    elif start_position == 'no': 
        num1 = answer

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Select operation: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    continue_c = input(f"Type 'y' to continue calculating with {answer},type 'new' for new calculation or type 'e' to exit.:")
    if continue_c.lower() == 'e':
        end_of_calculation = True
    elif continue_c.lower() == 'new':
        start_position = 'yes'
    elif continue_c == 'y':
        start_position = 'no'