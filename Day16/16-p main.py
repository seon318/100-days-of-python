from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    order = input(f"What do you want to drink? ({options}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)