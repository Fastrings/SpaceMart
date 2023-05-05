from json_interface import get_starting_inventory

class SpaceMart():

    # class attributes

    def __init__(self, budget):
        self.budget = budget
        self.days = 1
        self.products = []

        self.init_products(get_starting_inventory())
    
    def budget_check(self):
        if self.budget <= 0:
            exit("You ran out of money. Better luck next time!")

    def get_time_passed(self):
        return self.days

    def get_budget(self):
        return self.budget

    def add_time(self, days=1):
        self.days += days

    def pay_taxes(self):
        self.budget -= 30
        print(f"Remaining budget: {self.budget}")
    
    def init_products(self, inv):
        self.products.clear()
        for item in inv:
            self.products.append(item)