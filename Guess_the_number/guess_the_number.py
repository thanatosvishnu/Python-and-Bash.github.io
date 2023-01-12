from art import logo
import random


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def game():

    print(logo);
    print("Welcome to the number guessing game!");
    print("I'm thinking of a number between 1 and 100.")


    def level(lvl):
        if lvl == 'easy':
            return 10
        else:
            return 5;

    chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    lives = level(chosen_level);
    chosen_number = random.randint(0, 101);

    
    def check_guess(user_number, chosen_number, live):
        
        if user_number == chosen_number:
            print(f"You got it! The answer is {chosen_number}");
        

        elif user_number > chosen_number:
            print("Too high")
            return live-1;
                

        elif user_number < chosen_number:
            print("Too low")
            return live-1;
    user_number = 0;
    while  user_number!= chosen_number:
        
        print(f"You have {lives} attempts remaining to guess the number.")
        user_number = int(input("Guess the number: "));
        lives = check_guess(user_number, chosen_number, live= lives)
        if lives == 0:
            print("You run out of guesses, you lose")
            return
        elif user_number!= chosen_number:
            print("Guess again");
            

game();    
    
          
        
        

     