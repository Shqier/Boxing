import random

def boxing_game():
    punches = ['1', '2', '3', '4']
    
    player_choice = input("Choose your punch (1 for jab, 2 for cross, 3 for hook, 4 for uppercut): ")
    
    if player_choice not in punches:
        print("Invalid choice. Please choose from 1, 2, 3, or 4.")
        return
    
    player_choice = int(player_choice)
    opponent_choice = random.randint(1, 4)
    
    print(f"Player chose: {player_choice}")
    print(f"Opponent chose: {opponent_choice}")
    
    if player_choice == opponent_choice:
        print("It's a tie!")
    elif (player_choice == 1 and opponent_choice == 3) or \
         (player_choice == 3 and opponent_choice == 2) or \
         (player_choice == 2 and opponent_choice == 4) or \
         (player_choice == 4 and opponent_choice == 1):
        print("Player wins!")
    else:
        print("Opponent wins!")

boxing_game()
