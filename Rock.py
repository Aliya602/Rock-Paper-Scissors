# Rock, Paper and Scissors game

# importing useful libraries
import random
from colorama import Fore, Style, init
init()

print('==' * 50)
print(Fore.GREEN + 'Welcome to the Rock, Paper and Scissors Game!' + Style.RESET_ALL)
print('==' * 50)

# Defining the choices for the game
choices = ['rock', 'paper', 'scissors']



# Initialize scores and rounds
player_score = 0
computer_score = 0
rounds_played = 0

name = input('Please enter your name: ')
print(f'Hello, {name}! Let\'s start the game.')

while True:
    print(f'Is your name {name}? (yes/no)')
    name_confirm = input().lower()
    if name_confirm == 'no' or name_confirm == 'n':
        name = input('Please enter your name again: ')
        print(f'Hello, {name}! Let\'s start the game.')
    elif name_confirm == 'yes' or name_confirm == 'y':
        print(f'Great! Welcome, {name}! Let\'s start the game.')
        break
    else:
        print(Fore.RED + 'Invalid input! Please answer with yes or no.' + Style.RESET_ALL)

series_choice = input('Do you want to play a series of games? (yes/no): ').lower()
if series_choice == 'yes' or series_choice == 'y':
    best_of = int(input('How many rounds do you want to play? (e.g., 3, 5, 7): '))
    target_score = (best_of + 1) // 2  # Calculate the target score needed to win the series
    print(Fore.YELLOW + f'First to {target_score} wins the series!' + Style.RESET_ALL)
else:
    target_score = None

while True:
    print('==' * 50)
    print(Fore.CYAN + f'Round {rounds_played + 1}' + Style.RESET_ALL)
    print('==' * 50)

    player = input('Enter your choice (rock, paper, scissors): ').lower()

    if player == 'exit'or player == 'quit':
        print(Fore.YELLOW + 'Thanks for playing! Goodbye!' + Style.RESET_ALL)
        print(Fore.GREEN + f'Final Scores - {name}: {player_score}, Computer: {computer_score}' + Style.RESET_ALL)
        break
    if player not in choices:
        print(Fore.RED + 'Invalid choice! Please choose rock, paper, or scissors.' + Style.RESET_ALL)
        continue # Skip the rest of the loop and ask for input again


    computer = random.choice(choices)
    print(Fore.GREEN + f' 🖥️ Computer choice: {computer}' + Style.RESET_ALL)

    # Determine the winner
    if player == computer:
        print(Fore.YELLOW + 'It\'s a tie!' + Style.RESET_ALL)
    elif(player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print(Fore.GREEN + f'Congratulations, {name}! You win!' + Style.RESET_ALL)
        player_score += 1
    else:
        print(Fore.RED + f'Sorry, {name}. You lose!' + Style.RESET_ALL)
        computer_score += 1
    
    rounds_played += 1
    print(Fore.BLUE + f'Current Scores - {name}: {player_score}, Computer: {computer_score}' + Style.RESET_ALL)

    # Check if a player has reached the target score
    if target_score :
        if player_score >= target_score:
            print(Fore.GREEN + f'🎉Congratulations, {name}! You won the series!' + Style.RESET_ALL)
            break
        
        elif computer_score >= target_score:
            print(Fore.RED + '🖥️ Computer wins the series! Better luck next time!' + Style.RESET_ALL)
            break
    
    else:
        # Ask player if they want to play again after each round
        play_again = input('Do you want to play another round? (yes/no): ').lower()
        if play_again != 'yes' and play_again != 'y':
            print(Fore.YELLOW + 'Thanks for playing! Goodbye!' + Style.RESET_ALL)
            print(Fore.GREEN + f'Final Scores - {name}: {player_score}, Computer: {computer_score}' + Style.RESET_ALL)
            break
    
    

        