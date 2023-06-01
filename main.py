from src.spacemart import SpaceMart
import argparse, pyinputplus as pyip
import random, os, time
from src.json_interface import get_starting_inventory
from src.quiz_parser import pick_categories, pick_question

def fast_forward(jump, mart):
    current_time = mart.days
    mart.days += jump 
    cpt = 0
    for i in range(current_time, current_time + jump):
        if i % 30 == 0:
            cpt += 75000
        if i % 7 == 0:
            mart.apply_discounts()
            mart.make_sales(silent=True)

    mart.budget -= cpt
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Fast forwarded {jump} days in the future. In the meantime, you paid {cpt} space dollars in taxes.")
    print(f"Remaining budget: {mart.budget}")   

def print_event(msg):
    l = len(msg)
    border = "-" * (8 + l)
    print(border)
    print("|   " + msg + "   |")
    print(border)

def quiz(bet_amount, mart):
    categories = pick_categories()
    categ = pyip.inputMenu(categories, "Choose a category: \n", numbered=True)
    question, category, answer, choices = pick_question(categ)
    a = pyip.inputMenu(choices, question + "\n", lettered=True)
    if a == answer:
        mart.budget += bet_amount * 2
        print(f'Congratulations! You added {bet_amount * 2} space dollars to your budget')
    else:
        print(f'Wrong answer! The answer was: {answer}')
        print(f'You lost your bet of {bet_amount}')

    mart.days += 1    
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(mart):
    os.system('cls' if os.name == 'nt' else 'clear')
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
            mart.make_sales()

            menu_choices = ['Continue', 'Give up', 'Fast forward', 'Quiz Me!'] if mart.quiz_enabled else ['Continue', 'Give up', 'Fast forward']

            result = pyip.inputMenu(menu_choices, "What do you want to do?\n", numbered=True)
            match result:
                case 'Continue':
                    pass
                case 'Give up':
                    break
                case 'Fast forward':
                    result2 = pyip.inputNum(prompt="How many days in the future do you want to fast forward to? ")
                    fast_forward(result2, mart)
                    continue
                case 'Quiz Me!':
                    bet_amount = pyip.inputNum(prompt="How much money do you want to bet? ", min=0, max=mart.budget)
                    mart.budget -= bet_amount
                    quiz(bet_amount, mart)
                    continue
            os.system('cls' if os.name == 'nt' else 'clear')

        if days % 30 == 0: # pay taxes every month
            txt = "In total, " + "1 month has passed" if days == 30 else f"{int(days / 30)} months have passed"
            print(txt)
            print("You paid 150000 space dollars in taxes.")
            mart.init_products(get_starting_inventory())
            mart.pay_taxes()
        
        if days % 365 == 0: # actions every year
            mart.taxes -= 5000
            mart.inflation()
            mart.sales_reports = []
        
        mart.days += 1 # go forward 1 day in time
        mart.update_expiry_date() # update the remaining days before expiry of every product
        mart.throw_expired() # remove from products all expired ones

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Emulation of an inventory management system.")

    parser.add_argument("-b", "--budget", required=True, help="starting budget B of space mart", metavar="B")
    parser.add_argument("--quiz-enabled", required=True, help="Whether or not quizzes are enabled (Y/N)", choices={"Y", "N"})

    args = parser.parse_args()

    mart = SpaceMart(int(args.budget), quiz_enabled=(args.quiz_enabled == "Y"))
    print("This is the beginning of the program.")
    print(f"Your starting budget is: {mart.budget}.")
    print("Good luck!")
    print("-------------------------------------")
    time.sleep(2)
    main_loop(mart)