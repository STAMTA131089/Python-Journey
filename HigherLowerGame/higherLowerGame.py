from art import higher_lower
from config import data
import random
print(higher_lower)
#print(data)

choices = []
mydict = random.choice(data)
if len(choices)==0:
    choices.append(mydict['name'])
elif mydict['name'] not in choices:
    choices.append(mydict['name'])

def get_highest_follower():
    if data[a]['follower Count'] > data[b]['follower Count']:
        return "A"    
    else:
        return "B"

#print(choices)
is_game_over = False
score =0
while not is_game_over:
    a = random.randint(0,3)
    b = random.randint(0,3)
    
    print(f"compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
    print("Versus")
    print(f"Against b: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
    print(get_highest_follower().lower())
    guess = input("Who has more follower A or B? ").lower()
    
    if guess == get_highest_follower().lower():
        score +=1
    else:
        print(f"Game Over, You scored {score}")
        is_game_over = True




