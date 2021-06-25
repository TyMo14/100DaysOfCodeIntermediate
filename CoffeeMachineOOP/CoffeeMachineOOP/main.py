from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

run_machine = True

# Building out the code

while run_machine:
    prompt = input(f"What would you like? ({menu.get_items()}):")

if prompt == "of":
    run_machine = False

elif prompt == "report":
    coffee_maker.report()
    money_machine.report()

elif prompt in menu.get_items().split("/"):
    menu_item_obj = menu.find_drink(prompt)
    print(f"Your order costs ${menu_item_obj.cost}")

    if coffee_maker.is_resource_sufficient(menu_item_obj) and money_machine.make_payment(menu_item_obj.cost):
        coffee_maker.make_coffee(menu_item_obj)

else:
    run_machine = False
