from json_interface import get_starting_inventory
import numpy as np
from json_loader import TYPES
import random

class SpaceMart():

    def __init__(self, budget):
        self.budget = budget
        self.days = 1
        self.products = []
        self.current_report = {}
        self.bonus_taxes = 0
        self.sales_reduction = 0

        self.init_products(get_starting_inventory())

    def pay_taxes(self):
        self.budget -= 150000 + self.bonus_taxes
        print(f"Remaining budget: {self.budget}")

    def find_product_by_ref(self, ref):
        for p in self.products:
            if p['reference'] == ref:
                return p

    def compute_sales_result(self):
        total = 0
        if self.current_report != {}:
            rep = self.current_report
            for key, value in rep.items():
                ref = key
                sales_amount = value
                p = self.find_product_by_ref(ref)
                price = p['price'] - ((p['discount'] * p ['price']) // 100)
                total += price * sales_amount
        
        total = total - ((total * self.sales_reduction) // 100)
        return total

    def generate_sales_report(self):
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
    
    def restock(self, free = False):
        for p in self.products:
            p['quantity'] = 5
        
        if not free:
            self.budget -= 15000
    
    def apply_discounts(self):
        t = random.choice(TYPES)
        for p in self.products:
            p['discount'] = 0
            if p['type'] == t:
                p['discount'] = random.randint(0, 25)
    
    def update_expiry_date(self):
        for p in self.products:
            p['remaining_days'] -= 1
            if p['remaining_days'] <= 0:
                p['discount'] = 50

    def throw_expired(self):
        for p in self.products:
            if p['remaining_days'] == -3:
                self.products.remove(p)
    
    def pick_event(self):
        # 1: Loss of money
        # 2: Loss of stock
        # 3: More taxes
        # 4: Sales hindered
        # 5: Won the lottery
        # 6: Free delivery of products
        # 7: Rent is cheaper
        # 8: Sales get better
        return random.randint(1, 8)

    def apply_consequences(self, event):
        match event:
            case 1: 
                loss = random.randint(5000, 10000)
                self.budget -= loss
                msg = "Event: You lost " + str(loss) + " space dollars."
            case 2: 
                self.restock()
                msg = "Event: You lost your stock and had to pay to restock all your products."
            case 3:
                bonus = random.randint(5000, 10000)
                self.bonus_taxes += bonus
                msg = "Event: Taxes increased by " + str(bonus) + " space dollars."
            case 4:
                reduction = random.randint(1, 5)
                self.sales_reduction += reduction
                msg = "Event: Sales will be reduced by " + str(reduction) + "%."
            case 5: 
                win = random.randint(5000, 10000)
                self.budget += win
                msg = "Event: You won " + str(win) + " space dollars."
            case 6: 
                self.restock(free = True)
                msg = "Event: You got a free delivery of all your products."
            case 7:
                bonus = random.randint(5000, 10000)
                self.bonus_taxes -= bonus
                msg = "Event: Taxes decreased by " + str(bonus) + " space dollars."
            case 8:
                reduction = random.randint(1, 5)
                self.sales_reduction -= reduction
                msg = "Event: Sales will be increased by " + str(reduction) + "%."
        
        return msg

    def make_sales(self, silent=False):
        sales_report = self.generate_sales_report() # calculate next week's sales
        self.current_report = sales_report # the sales report is now the one for next week
        weekly_sales = self.compute_sales_result() #compute sales from report
        self.budget += weekly_sales
        if not silent:
            print(f"Weekly sales: {weekly_sales}")
        self.restock()