import random
import time

WORD=["python", "apple", "banana", "orange", "grapes",
    "computer", "keyboard", "mouse", "laptop", "screen",
    "school", "teacher", "student", "pencil", "book",
    "flower", "garden", "river", "mountain", "ocean",
    "sunshine", "rainbow", "storm", "weather", "season",
    "football", "cricket", "hockey", "tennis", "chess",
    "tiger", "elephant", "giraffe", "zebra", "monkey",
    "planet", "galaxy", "comet", "asteroid", "spaceship",
    "pizza", "burger", "noodle", "biscuit", "chocolate",
    "dance", "music", "guitar", "drums", "violin",
    "castle", "dragon", "sword", "magic", "wizard"]

class Hangman():

    def __init__(self):
        self.game_words=WORD
        self.guessed_letter=[]
        self.game_round=6
    
    def game_restart(self):
        self.guessed_letter=[]
        self.game_round=6
        self.game()
    
    def game_rules(self):
        print("\n"+"-"*13)
        print(f"{'HANGMAN':^13}")
        print("-"*13+"\n")
        print("INTRUCTIONS")
        print("1.You will have 6 lives to guess a word.")
        print("2.You have to enter only one letter else you gonna lose one live.")
        print("Best of luck.\n")

    def game(self):

        self.game_rules()
        time.sleep(0.4)
        print("Let The Game Begin's")
        word_choosed=random.choice(self.game_words)

        while self.game_round!=0:

            print(f"Your lives remaining {"❤️ "*self.game_round}\n")

            hint=""

            for char in word_choosed:
                if char in self.guessed_letter:
                    hint+=char
                else:
                    hint+="_"

            print(f"Word to guess:{hint}")

            if hint==word_choosed:
                print("You won the game. Congratulation\n")
                break

            while True:
                user_input=input("Enter a letter:").lower()
                if len(user_input)==1:
                    break
                else:
                    print("Enter one letter only.")
            time.sleep(0.2)
            
            if user_input in self.guessed_letter:
                print(f"You already guessed letter {user_input}")
                continue

            if user_input in word_choosed:
                self.guessed_letter.append(user_input)
                print(f"\nYou guessed right letter {user_input} is in the word.")
            else:
                self.game_round-=1
                print(f"\nYou enter letter {user_input} which is not in word.")
            
            if self.game_round==0:
                print("You lost all lives.Game Over!\n")
                print(f"Word was {word_choosed}")

hangman=Hangman()
hangman.game()
            




    
