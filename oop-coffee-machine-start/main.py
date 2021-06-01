from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

machine_is_on = True
while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino/) : ")
    if user_choice == "report":
        coffee_machine.report()
        money.report()
    elif user_choice == "off":
        print("Turning off for Maintenance")
        machine_is_on = False
        continue
    else:
        user_choice = menu.find_drink(user_choice)
        if user_choice is not None:
            is_enough_ingredients = coffee_machine.is_resource_sufficient(user_choice)
            is_payment_success = money.make_payment(user_choice.cost)
            if is_enough_ingredients and is_payment_success:
                coffee_machine.make_coffee(user_choice)
