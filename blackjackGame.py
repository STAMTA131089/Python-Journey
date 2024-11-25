import random
num_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def game():
    mylist = [random.choice(num_list) for i in range(2) ]
    print(f"Your Cards: {mylist}, current score: {sum(mylist)}")

    computer_list = []
    for s in range(2):
        computer_list.append(random.choice(num_list))

    print(f"Computer's first card: {computer_list[0]}")

    while sum(mylist)<21:
        x = input("type 'y' to get another card, type n to pass: ").lower()
        if x == 'y':
            mylist.append(random.choice(num_list))
            print(f"Your Cards: {mylist}, current score: {sum(mylist)}")
            print(f"Computer's first card: {computer_list[0]}")

    while sum(computer_list)<21:
        computer_list.append(random.choice(num_list))
    
    print(f"your final hand is {mylist} and final score is {sum(mylist)}")
    print(f"computer final hand is {computer_list} and computer final score is {sum(computer_list)}")

    if sum(mylist) > sum(computer_list):
        print("you won")
    elif sum(mylist) == sum(computer_list):
        print( "it is a draw")
    else:
        print("Computer won, you lose")




continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n'").lower()
if continue_game == 'y':
    game()
elif continue_game == 'n':
    print("Game Over")
else:
    print("provide either y or n")


