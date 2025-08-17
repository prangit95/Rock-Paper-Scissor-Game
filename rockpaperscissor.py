"""
    WORKFLOW OF THE PROJECT:
    
    1. User selects either Rock, Paper, or Scissors. (user input)
    2. Computer randomly selects Rock, Paper, or Scissors.
    3. Determine the winner based on the rules:
        - Rock crushes Scissors
        - Scissors cuts Paper
        - Paper covers Rock
    4. Display the result to the user.
    
    Cases:
    A - Rock
    rock vs rock = Draw
    rock vs paper = paper wins
    rock vs scissors = rock wins

    B - Paper
    paper vs paper = Draw
    paper vs rock = paper wins
    paper vs scissors = scissors wins

    C - Scissors
    scissors vs scissors = Draw
    scissors vs rock = rock wins
    scissors vs paper = scissors wins
    
    """
    
import random
item_list = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your choice: Rock, Paper, Scissors:")
comp_choice = random.choice(item_list)

print(f"User Choice: {user_choice}")
print(f"Computer Choice: {comp_choice}")

if user_choice == comp_choice:
    print("Both choose same : Match is drawn")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock : Computer wins")
    else:
        print("Rock crushes Scissors : You win")
elif user_choice == "Paper":
    if comp_choice == "Scissors":
        print("Scissors cuts Paper : Computer wins")
    else:
        print("Paper covers Rock : You win")
elif user_choice == "Scissors":
    if comp_choice == "Rock":
        print("Rock crushes Scissors : Computer wins")
    else:
        print("Scissors cuts Paper : You win")