class Stock:
    # ------- CONSTRUCTOR -------
    def __init__(self, coffee=100, milk=200, water=300, profit=0.0):
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.profit = profit

    def __str__(self):
        return (
            "IN STOCK:\n"
            f"Coffee: {self.coffee}\n"
            f"Milk: {self.milk}\n"
            f"Water: {self.water}\n"
            "\n"
            f"PROFIT: ${self.profit}"
        )

    # ------- METHODS -------
    # Check if the machine has enough resources
    def is_resource_sufficient(self, selected_drink):
        if (selected_drink.coffee > self.coffee
                or selected_drink.milk > self.milk
                or selected_drink.water > self.water):

            print("Insufficient resources!")
            return False

        else:
            print(selected_drink)
            return True

    def adjust_stock(self, choice):
        self.coffee -= choice.coffee
        self.milk -= choice.milk
        self.water -= choice.water
        self.profit += choice.cost
