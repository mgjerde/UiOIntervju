items = [ 'Dagens', 'Vegetar', 'Halal' ]
prices = [ 53.90, 42.50, 59.90 ]
meal_sum = 0
total_sum = 0

def sell(item):
    global meal_sum
    global total_sum
    if item == 'Dagens':
        meal_sum += prices[0]
        total_sum += prices[0]
        print("Dagens, here you go.\n")
    elif item == 'Vegetar':
        meal_sum += prices[1]
        total_sum += prices[1]
        print("Vegetar, here you go.\n")
    elif item == 'Halal':
        meal_sum += prices[2]
        total_sum += prices[2]
        print("Halal, here you go.\n")
    else:
        print("%s is not on the menu!\n" % item)

def empty_cash_registry():
    global meal_sum
    meal_sum = 0
    print("Cash registry emptied. Thieves be warned!\n")

def cafeteria():
    global meal_sum
    global total_sum
    print("What would you like today? (type 'how is business?' to attempt small talk, or 'not hungry' to stop)")
    user_input = input("> ")
    while user_input != 'not hungry':
        question = 0
        if user_input == 'how is business?':
            question = 1
            if total_sum == 0:
                print("Not good so far. No one seems to be hungry today!\n")
            elif total_sum > 0 and total_sum <= 500:
                print("Alright. Could have been better\n")
            elif total_sum > 500:
                print("Excellent! Lots of hungry students around today.\n")
        if question == 0:
            sell(user_input)
        if meal_sum > 200:
            empty_cash_registry()
        print("What would you like today? (type 'how is business?' to attempt small talk, or 'not hungry' to stop)")
        user_input = input("> ")
    print("Welcome back later!\n")

if __name__ == '__main__':
    cafeteria()


