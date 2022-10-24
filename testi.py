import random as rd
def game():
    level=input("Welcome to number guessing game! Type 'easy' for easy mode and 'hard' for hard mode")
    while level.lower() not in ('easy','hard'):
        level=input("Type 'easy' for easy mode and 'hard' for hard mode").lower()
        
    if level.lower()=='easy':
        attempts=10
    else:
        attempts=5
    
    number=rd.randint(1,100)

    game_over=False

    while not game_over:
        print(f"You have {attempts} guesses left.")
        guess=int(input("guess a number between 1 and 100"))
        if guess==number:
            print(f"Correct! You win! The number was {guess}.")
            game_over=True
        elif guess>100 or guess<1:
            print("Guess is out of range, guess again")
        elif guess>number:
            print("Too high.")
            attempts-=1
            if attempts==0:
                print(f"You run out of guesses, you lose. The correct number was {number}.")
                game_over=True
            else:
                print("Guess again.")
        else:
            print("Too low.")
            attempts-=1
            if attempts==0:
                print(f"You run out of guesses, you lose. The correct number was {number}.")
                game_over=True
            else:
                print("Guess again.")
    
    if input("Type 'y' to play again").lower()=="y":
        game()

game()