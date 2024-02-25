import random

def boxing_game(is_championship):
    rounds = 12 if is_championship else 3
    
    for round in range(1, rounds + 1):
        print(f"\nRound {round} - Fight!")
        
        player_punches = []
        for _ in range(3):  # Allowing up to 3 punches per round
            player_choice = input("Choose your punch (1 for jab, 2 for cross, 3 for hook, 4 for uppercut, or 0 to end round): ")
            
            if player_choice == '0':
                break
            
            if player_choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please choose from 1, 2, 3, 4, or 0 to end round.")
                continue
            
            player_punches.append(int(player_choice))
        
        computer_punches = [random.randint(1, 4) for _ in range(len(player_punches))]
        
        print("\nPlayer's punches:", player_punches)
        print("Computer's punches:", computer_punches)
        
        for player_punch, computer_punch in zip(player_punches, computer_punches):
            if player_punch == computer_punch:
                print("It's a tie!")
            elif (player_punch == 1 and computer_punch == 3) or \
                 (player_punch == 3 and computer_punch == 2) or \
                 (player_punch == 2 and computer_punch == 4) or \
                 (player_punch == 4 and computer_punch == 1):
                print("Player wins this punch!")
            else:
                print("Computer wins this punch!")

# Simulating a championship fight with 12 rounds
print("Championship Fight:")
boxing_game(is_championship=True)

# Simulating a regular fight with 3 rounds
print("\nRegular Fight:")
boxing_game(is_championship=False)
