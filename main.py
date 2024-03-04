# ------- IMPORTS -------
from stock import Stock
from drink import Drink

# ------- INSTANCES -------
# Instance of Stock
stock = Stock()

# Dictionary and instances of Drinks
drinks = {
    "cappuccino": Drink("Cappuccino", 24, 100, 250, 3.0),
    "espresso": Drink("Espresso", 18, 0, 50, 1.5),
    "latte": Drink("Latte", 24, 200, 150, 2.5)
}


# ------- FUNCTIONS -------
# Process the customer choice
def process_customer_choice(choice):
    selected_drink = drinks.get(choice)

    # If drink exists in the dictionary
    if selected_drink:
        return stock.is_resource_sufficient(selected_drink)
    else:
        print("\nInvalid Choice! Try again.")
        return False


# Returns the total calculated from coins inserted
def process_coins():
    print("\nPlease, insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


# True if money is sufficient or False if not
def is_transaction_successful(money_received, choice):
    drink_cost = drinks.get(choice).cost
    drink_name = drinks.get(choice).name

    # If money is sufficient
    if money_received >= drink_cost:
        # If money is more than enough
        if money_received > drink_cost:
            print(f"\nHere is your change. ${round(money_received - drink_cost, 2)}")

        return True

    # If money is not sufficient
    else:
        print(f"\nSorry, that's not enough money. Money refunded. ${money_received}")
        return False


# ------- MAIN LOOP -------
is_machine_on = True

while is_machine_on:
    # Report to the user
    customer_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    customer_choice = customer_choice.lower()

    # Secret code for maintenance. Turns off the machine.
    if customer_choice == "off":
        is_machine_on = False

    # Secret code for maintenance. Returns available ingredients and profit.
    elif customer_choice == "report":
        print(stock)

    # Returns depending on the drink
    else:
        if process_customer_choice(customer_choice):
            money_inserted = process_coins()
            if is_transaction_successful(money_inserted, customer_choice):

                # Adjust the stock based on the purchase
                stock.adjust_stock(drinks.get(customer_choice))
                print(f"\nHere is your drink!")
