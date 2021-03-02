import random

user_choice = ""
score = {}


def winner(user, computer, all_options):
    detect_winner = all_options[all_options.index(user) + 1:] + all_options[:all_options.index(user)]
    if user == computer:
        return 0
    elif computer in detect_winner[:int(len(detect_winner)/2)]:
        return -1
    else:
        return 1


def get_rating(arg_name):
    if arg_name in score.keys():
        return score[arg_name]
    else:
        return 0


name = input("Enter your name:")
print(f"Hello, {name}")

options_string = input()
if options_string:
    options = options_string.split(",")
else:
    options = ["rock", "paper", "scissors"]

print("Okay, let's start")

rating = open("rating.txt", "r")
for users in rating:
    score[users.split()[0]] = int(users.split()[1])

while user_choice != "!exit":
    computer_choice = random.choice(options)
    user_choice = input()
    if user_choice == "!exit":
        break
    elif user_choice == "!rating":
        print(f"Your rating: {get_rating(name)}")
    elif user_choice not in options:
        print("Invalid input")
    elif winner(user_choice, computer_choice, options) == 0:
        print(f"There is a draw ({computer_choice})")
        score[name] += 50
    elif winner(user_choice, computer_choice, options) == 1:
        print(f"Well done. The computer chose {computer_choice} and failed")
        score[name] += 100
    elif winner(user_choice, computer_choice, options) == -1:
        print(f"Sorry, but the computer chose {computer_choice}")

print("Bye!")
rating.close()
