import random

computer_guess = random.randint(1,100)
print(computer_guess)
print(f"Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game(attempts:int):
    should_continue = True
    for i in range(attempts,0,-1):
        user_input = int(input("Make a guess: "))
        
        if user_input == computer_guess:
            print("you guessed it right")
            return
        elif user_input > computer_guess:
            print("too high")
        else:
            print("too low")        
        
        if i !=1:
            print(f"you have {i-1} attempts left")
    print("you lose")
if user_input == "hard":
    game(5)
else:
    game(10)

