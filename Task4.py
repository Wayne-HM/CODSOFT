#Task 4-Rock Paper Scissors Game
import random
def computerchoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif(user_choice == 'rock' and computer_choice == 'scissors'):
        return 'user'
    elif(user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    elif(user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print("You chose: ",user_choice)
    print("Computer chose: ",computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock/paper/scissors.")
            continue
        computer_choice = computerchoice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        print("\nScores:\nYou:",user_score,"\nComputer:",computer_score)
        play_again = input("\nDo you want to play another round? (yes/no): ")
        if play_again == 'no':
            print("Thanks for playing!")
            break
main()
