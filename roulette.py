import random
colours = ["green", "red", "blue"]
dozen = ["1st","2nd","3rd"]
choice = ["number", "dozen", "colour", "other"]

total_money = 10000

result_colour = random.choice(colours)
result_number = random.randint(0, 36)

def __init__():
    place_bet()

def place_bet():
    bet = int(input("how much money do you want to bet"))
    if bet > total_money:
        print("invalid")
        while bet > total_money:
            bet = int(input("how much money do you want to bet"))
    choice = input("what choice do you want to make (choose from: number, dozen, colour or other)")
    choice = choice.lower()
    get_result(choice)

def get_result(choice):
    if choice == "number":
        print(result_number)
        input_number = int(input("choose a number"))
        if input_number == result_number:
            print("you won")
        else:
            print("you lost, unlucky")
    elif choice == "colour":
        print(result_colour)
    else:
        print("test")
    __init__()

__init__()
