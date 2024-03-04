# ------- IMPORTS -------
from abc import ABC


class Drink(ABC):
    # ------- CONSTRUCTOR -------
    def __init__(self, name, coffee, milk, water, cost):
        self.name = name
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.cost = cost

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Ingredients: Coffee: {self.coffee}, Milk: {self.milk}, Water: {self.water}\n"
            f"Cost: ${self.cost}\n"
        )
