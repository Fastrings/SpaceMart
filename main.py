from spacemart import SpaceMart
import argparse, pyinputplus as pyip

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
    
def init(mart):
    print("This is the beginning of the program.")
    print(f"Your total budget is: {mart.get_budget()}.")
    print("Good luck!")
    print("-------------------------------------")

def main_loop(mart):
    init(mart)
    while True:
        days = mart.get_time_passed() # updating time passed
        budget = mart.get_budget() # updating current budget

        mart.budget_check() # checking if we still have money

        if days % 7 == 0: # interact with user every week
            print(f"This is day {days}.")
            cont, ff =  user_interaction(mart)
            if not cont:
                break
            else:
                if ff != 0:
                    mart.add_time(ff)
                    continue
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

    mart = SpaceMart(int(args.budget))
    main_loop(mart)