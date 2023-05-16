from json_interface import get_starting_inventory
import numpy as np

class SpaceMart():

    # class attributes

    def __init__(self, budget):
        self.budget = budget
        self.days = 1
        self.products = []
        self.current_report = {}

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
        self.budget -= 150000
        print(f"Remaining budget: {self.get_budget()}")

    def find_product_by_ref(self, ref):
        for p in self.products:
            if p['reference'] == ref:
                return p
    
    def make_money(self):
        total = 0
        if self.current_report != {}:
            rep = self.current_report
            for key, value in rep.items():
                ref = key
                sales_amount = value
                p = self.find_product_by_ref(ref)
                price = p['price']
                total += price * sales_amount
        
        self.budget += total

    def update_report(self, report):
        self.current_report = report

    def calculate_sales(self):
        sales_report = {}
        daily_sales = np.random.default_rng().normal(10, 3, 7)
        weekly_sales = sum(daily_sales)
        cpt = weekly_sales

        while cpt > 0:
            rem = np.array([product for product in self.products if product['quantity'] > 0])
            if len(rem) == 0:
                break
            c = np.random.default_rng().choice(a=rem)
            ref = c['reference']
            # quantity - 1
            ind = rem.tolist().index(c)
            if rem[ind]['quantity'] > 0:
                rem[ind]['quantity'] -= 1
            if ref in sales_report: # add reference to report
                sales_report[ref] += 1
            else:
                sales_report[ref] = 1

            cpt -= 1

        return sales_report

    def init_products(self, inv):
        self.products.clear()
        for item in inv:
            self.products.append(item)