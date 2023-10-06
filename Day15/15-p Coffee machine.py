MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

def make_coffee(coffee):
    for key in resources:
        resources[key] -= MENU[coffee]['ingredients'][key]
    print(f"Here is your {coffee}☕ Enjoy.")

# coin = quarter, dime, nickle, penny
def payment(coffee):
    total = 0
    print("Please insert coins")
    for key in coins:
        a = int(input(f"How many {key}?: "))
        total += round(coins[key]*a)
    if total < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total > MENU[coffee]['cost']:
        print(f"Here is ${total-MENU[coffee]['cost']} in change")
        make_coffee(coffee)
        return total
    else:
        make_coffee(coffee)
        return total

# sufficiency
def check(coffee):
    for key in resources:
        if resources[key] < MENU[coffee]['ingredients'][key]:
            return False
            print(f"Sorry there is not enough {key}")
        return True

turn_off = False
# ask user “What would you like? (espresso/latte/cappuccino):”
while not turn_off:
    order = input("What would you like? (espresso/latte/cappuccino): ")
# Turn off the Coffee Machine by entering “off” to the prompt.
    if order == "off":
      turn_off = True
# print report
    elif order == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${money}")

    elif order == "espresso" or "latte" or "cappuccino":
        check(order)
        if check(order):
            payment(order)
            money += payment(order)
