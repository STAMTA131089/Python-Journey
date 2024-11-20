#listPractice
import random
# Rock, papers and Scissors game
#   0     1          2

rock = """
                      __    
_______  ____   ____ |  | __
\_  __ \/  _ \_/ ___\|  |/ /
 |  | \(  <_> )  \___|    < 
 |__|   \____/ \___  >__|_ \ 
                   \/     \/
"""

papers = """
                                         
___________  ______   ___________  ______
\____ \__  \ \____ \_/ __ \_  __ \/  ___/
|  |_> > __ \|  |_> >  ___/|  | \/\___ \ 
|   __(____  /   __/ \___  >__|  /____  >
|__|       \/|__|        \/           \/ """

scissors = """
              .__                                  
  ______ ____ |__| ______ _________________  ______
 /  ___// ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 \___ \\  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
/____  >\___  >__/____  >____  >____/|__|  /____  >
     \/     \/        \/     \/                 \/ 
     """

myinput = int(input("please enter 0 for Rock, 1 for papers and 2 for scissors "))
program_input = int(random.randint(0,2))
print(f"your input is {rock}")
if program_input == 0:
    pc = rock
elif program_input ==1:
    pc = papers
else:
    pc = scissors
print(f"Computer input is {pc}")


if myinput == 0:
    if program_input ==0:
        print(f"it is a draw. Try again")
    elif program_input == 1:
        print(f"you lose")
    else:
        print("you won")
