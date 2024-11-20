import random

word_list = ["aardvark","baboon","camel"]
chosen_word =random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)


final_word = ""

game_over = False

while not game_over:
    guess = (input("Guess a letter\n")).lower()
    placeholder=""
    for letter in chosen_word:
        if letter == guess:
            placeholder += guess
            final_word+=guess   
        elif letter in final_word:
            placeholder += letter
        else:
            placeholder += "_"
    print(placeholder)
    if "_" not in placeholder:
        game_over = True
    print(final_word)
