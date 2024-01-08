import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        play_game()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        score = 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        score = 1
    else:
        print("Computer wins!")
        score = -1

    


    with open("score.txt", "w+") as f:
        
        total_score_str = f.read()

        if total_score_str:
            total_score = int(total_score_str)
        else:
            total_score = 0

        total_score += score

        
        f.seek(0)  
        f.write(str(total_score))
        print(f"Your score is: {total_score}")


play_game()
play = input("Do you want to play again? (y/n): ").lower()
if play == 'y':
    play_game()

else:
    print("Thanks for playing!")
