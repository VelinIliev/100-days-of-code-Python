# Espresso - 50 ml water - 18g Coffee - $1.50
# Latte - 200 ml water - 24g Coffee - 150 ml milk - $ 2.50
# Cappuccino = 250ml water - 24g coffee - 100ml milk - $3.00
# penny = 0.01, nickel = 0,05, Dime = 0.10, Quarter = 0.25

from project_data import MENU, resources

profit = 0


def calculate_change():
    print("Please insert coins.")
    sum = int(input("how many quarters?:")) * 0.25
    sum += int(input("how many dimes?:")) * 0.10
    sum += int(input("how many nickles?:")) * 0.05
    sum += int(input("how many pennies?:")) * 0.01
    change = sum - new_drink_price
    if change >= 0:
        return change
    else:
        return False

def substract_resources(new_drink_resources):
    if 'water' in new_drink_resources:
        resources['water'] -= new_drink_resources['water']
    if 'milk' in new_drink_resources:
        resources['milk'] -= new_drink_resources['milk']
    if 'coffee' in new_drink_resources:
        resources['coffee'] -= new_drink_resources['coffee']
    print(f"water: {resources['water']}, milk: {resources['milk']}, coffee: {resources['coffee']} ")


def check_resources(new_drink_resources):
    for item in new_drink_resources:
        if new_drink_resources[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


while True:
    choice = input("What would you like? (espresso/latte/cappuccino)")

    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        new_drink_resources = MENU[choice]['ingredients']
        new_drink_price = MENU[choice]['cost']

        if check_resources(new_drink_resources) == False:
            break
        else:
            change = calculate_change()

            if change >= 0:
                print(f"Here is ${change:.2f} in change.")
                substract_resources(new_drink_resources)
                profit += new_drink_price
            else:
                print(f"Sorry that's not enough money. Money refunded")
                break

            print(f'Here is your {choice}. Enjoy')

    elif choice == 'report':
        print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nprofit: {profit:.2f}")
    elif choice == 'off':
        print("Goodbye!")
        break
    else:
        print("We don't have such drink.")





