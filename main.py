def user_interaction(budget):
    x = input(f"Remaining budget: {budget}.\nDo you want to continue? (Y/N)")
    return (x == 'Y') 

def init(budget):
    print("This is the beginning of the program.")
    print(f"Your total budget is: {budget}.")
    print("Good luck!")

def main_loop(budget):
    days = 1
    init(budget)
    while True:
        if budget < 0:
            print("You are out of money. Better luck next time!")
            break
        if days % 7 == 0:
            print(f"This is day {days}.")
            if not user_interaction(budget):
                break
        if days % 30 == 0:
            txt = "1 month has passed" if days == 30 else f"{int(days / 30)} months have passed"
            print(txt)
            print("You pay 30 space dollars in taxes.")
            budget -= 30
        days += 1

if __name__ == '__main__':
    main_loop(100)