import random
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Main Program
def rock_paper_scissors():
    print(Fore.MAGENTA + "\n====== Rock-Paper-Scissors Game ======\n")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    rounds = int(input(Fore.CYAN + "How many rounds would you like to play?: " + Fore.WHITE))

    for _ in range(rounds):
        print(Fore.CYAN + "\nChoices: Rock | Paper | Scissors")
        user_choice = input(Fore.YELLOW + "Choose your move: " + Fore.WHITE).lower()
        
        if user_choice not in choices:
            print(Fore.RED + "Invalid choice! Please choose rock, paper, or scissors.\n")
            continue
        
        computer_choice = random.choice(choices)
        print(Fore.CYAN + f"\nYou chose: {user_choice.capitalize()}")
        print(Fore.CYAN + f"Computer chose: {computer_choice.capitalize()}\n")
        
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print(Fore.YELLOW + "It's a tie!\n")
        elif result == "user":
            print(Fore.GREEN + "You win this round!\n")
            user_score += 1
        else:
            print(Fore.RED + "Computer wins this round!\n")
            computer_score += 1
        
        print(Fore.CYAN + f"Score: You {user_score} - Computer {computer_score}\n")
    
    # Final result after all rounds
    if user_score > computer_score:
        print(Fore.GREEN + "\nCongratulations! You won the game!\n")
    elif user_score < computer_score:
        print(Fore.RED + "\nComputer wins the game! Better luck next time!\n")
    else:
        print(Fore.YELLOW + "\nIt's a tie game!\n")
    
    reset_game = input(Fore.CYAN + "Do you want to reset and play again? (yes/no): " + Fore.WHITE).lower()
    if reset_game == 'yes':
        rock_paper_scissors()
    else:
        print(Fore.CYAN + "Goodbye! Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
