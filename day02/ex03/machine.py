import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.drinks_served = 0
        self.max_drinks = 10
        self.is_broken = False

    def repair(self):
        self.is_broken = False
        self.drinks_served = 0
        print("------------------------------------------------------------------------------")
        print("The machine has been repaired. Ready to continue!")
        print("------------------------------------------------------------------------------\n")

    def serve(self, drink_class):
        if self.is_broken:
            raise self.BrokenMachineException()

        self.drinks_served += 1

        if self.drinks_served > self.max_drinks:
            self.is_broken = True
            self.drinks_served = 0
            raise self.BrokenMachineException()

        return drink_class() if random.randint(0, 1) == 0 else self.EmptyCup()

if __name__ == "__main__":
    machine = CoffeeMachine()

    try:
        for _ in range(22):
            try:
                drink = machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
                print(drink)
            except machine.BrokenMachineException:
                print("------------------------------------------------------------------------------")
                print("Machine is broken. Please repair it.")
                machine.repair()
    except KeyboardInterrupt:
        print("The machine needs repair.")
