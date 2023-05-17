from spacemart import SpaceMart
import argparse, pyinputplus as pyip
import random
from json_interface import get_starting_inventory


def user_interaction(mart):
    result = pyip.inputMenu(['Continue', 'Give up', 'Fast forward'], "What do you want to do?\n", numbered=True)
    match result:
        case 'Continue':
            return (True, 0)
        case 'Give up':
            return (False, 0)
        case 'Fast forward':
            result2 = pyip.inputNum(prompt="How many days in the future do you want to fast forward to?")
            return (True, result2)
        case _:
            pass

def fast_forward(current_time, jump):
    mart.days += jump
    cpt = 0
    for i in range(current_time, current_time + jump):
        if i % 30 == 0:
            cpt += 30

    mart.budget -= cpt
    print(f"Fast forwarded {jump} days in the future. In the meantime, you paid {cpt} space dollars in taxes.")
    print(f"Remaining budget: {mart.budget}")

def init(mart):
    print("This is the beginning of the program.")
    print(f"Your total budget is: {mart.budget}.")
    print("Good luck!")
    print("-------------------------------------")

def print_event(msg):
    l = len(msg)
    border = "-" * (8 + l)
    print(border)
    print("|   " + msg + "   |")
    print(border)
    
def main_loop(mart):
    init(mart)
    while True:
        days = mart.days # updating time passed

        if mart.budget <= 0: # checking if we still have money
            exit("You ran out of money. Better luck next time!")

        if random.randint(1, 100) == 42 and days % 2 == 0:
            event_number = mart.pick_event()
            msg = mart.apply_consequences(event_number)
            print_event(msg)

        if days % 7 == 0: # interact with user every week
            print(f"This is day {days}.")

            mart.apply_discounts()
            sales_report = mart.generate_sales_report() # calculate next week's sales
            mart.current_report = sales_report # the sales report is now the one for next week
            weekly_sales = mart.compute_sales_result()
            mart.budget += weekly_sales
            print(f"Weekly sales: {mart.compute_sales_result()}")

            cont, ff =  user_interaction(mart)
            if not cont:
                break
            else:
                if ff != 0:
                    fast_forward(days, ff)
                    continue
            mart.restock()

        if days % 30 == 0: # pay taxes every month
            txt = "1 month has passed" if days == 30 else f"{int(days / 30)} months have passed"
            print(txt)
            print("You paid 150000 space dollars in taxes.")
            mart.init_products(get_starting_inventory())
            mart.pay_taxes()
        
        mart.days += 1 # go forward 1 day in time
        mart.update_expiry_date() # update the remaining days before expiry of every product
        mart.throw_expired() # remove from products all expired ones

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Emulation of an inventory management system.")

    parser.add_argument("-b", "--budget", required=True, help="starting budget B of space mart", metavar="B")

    args = parser.parse_args()

    mart = SpaceMart(int(args.budget))
    main_loop(mart)