import random

game=["rock","paper","scissor"]

def print_score(user_win, computer_win):
    print(f"Score: You {user_win} | Computer {computer_win}\n")

def input_rps():

    while True:
        user_input=input("\nEnter Rock/Paper/Scissor:").lower()
        if user_input in game:
            return user_input
        print("Enter rock or paper or scissor.") 
    
def get_score_rps(user_input,computer_choice,user_win,computer_win):

    if user_input=='rock' and computer_choice=='scissor':
        print("You won the round")
        user_win+=1
        return user_win,computer_win
    
    elif user_input=='scissor' and computer_choice=='paper':
        print("You won the round")
        user_win+=1
        return user_win,computer_win
    
    elif user_input=='paper' and computer_choice=='rock':
        print("You won the round")
        user_win+=1
        return user_win,computer_win
    else:
        print("You lose the round")
        computer_win+=1
        return  user_win,computer_win
    
def rps1(levels):
    user_win =0
    computer_win=0

    for level in range(1,levels+1):

        print(f"\nRound {level}")
        computer_choice=random.choice(game)
        user_choice=input_rps()

        print(f"You chose {user_choice.title()}")
        print(f"Computer chose {computer_choice.title()}")

        if user_choice==computer_choice:
            print("It's a draw") 
        else:
            user_win,computer_win=get_score_rps(user_choice,computer_choice,user_win,computer_win)

        print_score(user_win, computer_win)

    if user_win>computer_win:
        print(f"You won the game. Your score was {user_win} and Computer score was {computer_win}. ")        
    elif computer_win>user_win:
        print(f"You lost the game. Your score was {user_win} and Computer score was {computer_win}.")          
    else:
        print(f"It's a draw. Your score was {user_win} and Computer score was {computer_win}.")

def rps2(rounds):
    user_win =0
    computer_win=0

    print(f"\nFirst to win {rounds} wins.")

    while True:

        computer_choice=random.choice(game)
        user_choice=input_rps()

        print(f"You chose {user_choice.title()}")
        print(f"Computer chose {computer_choice.title()}") 

        if user_choice==computer_choice:
            print("It's a draw")
        else:
            user_win,computer_win=get_score_rps(user_choice,computer_choice,user_win,computer_win)

        print_score(user_win, computer_win)

        if user_win==rounds:
            print(f"\nYou won the game. You won {user_win} round and Computer won {computer_win} round.")
            break

        elif computer_win==rounds:
            print(f"\nYou lost the game. You won {user_win} round and Computer won {computer_win} round.")
            break

print("\nWelcome To Rock Paper Scissor Simulator\n")

game_over=False

rps_available=["Normal Rock/Paper/Scissor","First to win n round wins Rock/Paper/Scissor"]

while not game_over:

    for i,rps in enumerate(rps_available,start=1):
        print(f"{i}.{rps}")
    
    try:
        which_game=int(input("\nEnter which game to play:"))
    except ValueError:
        print("Enter numeric value only.")
        continue

    if which_game==1:
        try:
            game_rounds=int(input("\nEnter the no. of rounds do you want to play:"))
        except ValueError:
            print("Enter numeric value only.\n")
            continue

        if game_rounds>0:
            rps1(game_rounds)
        else:
            print("Invalid game_round")

    elif which_game==2:
        try:
            rounds=int(input("\nEnter the number of rounds needed to win:"))
        except ValueError:
            print("Enter numeric value only.\n")
            continue
       
        if rounds>0:
            rps2(rounds)
        else:
            print("Invalid game_round")

    else:
        print("Enter valid input.")

    while True:
        new_game=input("\nDo you want play one more game type 'y' for yes and 'n' for no:").lower()
        if new_game in ['n','y']:
            break
        else:
            print("Enter valid option.")

    if new_game=='n':
        print("Thanks for playing.\n")
        game_over=True
       