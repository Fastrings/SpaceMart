def user_interaction():
    x = input("Do you want to continue? (Y/N)")
    return (x == 'Y') 

def init(budget):
    print("This is the beginning of the program.")
    print(f"Your total budget is: {budget}.")
    print("Good luck!")

def main_loop(budget):
    days = 1
    init(budget)
    while True:
        if days % 7 == 0:
            print(f"This is day {days}.")
            if not user_interaction():
                break
        days += 1

if __name__ == '__main__':
    main_loop(10000)