from spacemart import SpaceMart
import argparse

def user_interaction(budget):
    x = input(f"Remaining budget: {budget}.\nDo you want to continue? (Y/N)")
    return (x == 'Y') 

def init(budget):
    print("This is the beginning of the program.")
    print(f"Your total budget is: {budget}.")
    print("Good luck!")

def main_loop(mart):
    init(mart.get_budget())
    while True:
        days = mart.get_time_passed() # updating time passed
        budget = mart.get_budget() # updating current budget

        mart.budget_check() # checking if we still have money

        if days % 7 == 0: # interact with user every week
            print(f"This is day {days}.")
            if not user_interaction(budget):
                break
        if days % 30 == 0: # pay taxes every month
            txt = "1 month has passed" if days == 30 else f"{int(days / 30)} months have passed"
            print(txt)
            print("You paid 30 space dollars in taxes.")
            mart.pay_taxes()
        
        mart.add_time() # go forward in time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Emulation of an inventory management system.")

    parser.add_argument("-b", "--budget", required=True, help="starting budget B of space mart", metavar="B")

    args = parser.parse_args()
    budget = args.budget

    mart = SpaceMart(budget)
    main_loop(mart)