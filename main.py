from resources import *


def check_resources(coffee):
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print("I'm sorry, there is not enough water.")
        return False
    else:
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("I'm sorry, there is not enough milk.")
            return False
        else:
            if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
                print("I'm sorry, there is not enough coffee")
                return False
            else:
                return True


def calculate_transaction(total_amount):
    if total_amount >= MENU[user_choice]["cost"]:
        change = float(total_amount - MENU[user_choice]["cost"])
        resources["money"] += MENU[user_choice]["cost"]
        print(f"Here is $ {round(change, 2)} in change.")
        return True


while True:
    choices = ["espresso", "latte", "cappuccino", "off"]
    user_choice = None
    while user_choice not in choices:
        user_choice = input("What would you like? (espresso / latte / cappuccino) ").lower()
        if user_choice == "report":
            print("Water:", resources["water"], "ml")
            print("Milk:", resources["milk"], "ml")
            print("Coffee:", resources["coffee"], "g")
            print("Money:", "$", resources["money"])
    if user_choice == "off":
        print("You turned off the coffee machine.")
        break
    make_coffee = check_resources(user_choice)
    if make_coffee:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        money = calculate_transaction(total_amount)
        if money:
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            print("Enjoy your coffee!\n")
