import random

def boxing_game(rounds):
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

        opponent_punches = [random.randint(1, 4) for _ in range(len(player_punches))]

        print("\nPlayer's punches:", player_punches)
        print("Opponent's punches:", opponent_punches)

        for player_punch, opponent_punch in zip(player_punches, opponent_punches):
            if player_punch == opponent_punch:
                print("It's a tie!")
            elif (player_punch == 1 and opponent_punch == 3) or \
                 (player_punch == 3 and opponent_punch == 2) or \
                 (player_punch == 2 and opponent_punch == 4) or \
                 (player_punch == 4 and opponent_punch == 1):
                print("Player wins this punch!")
            else:
                print("Opponent wins this punch!")

# Allowing the user to choose between championship or regular fight
fight_type = input("Enter 'c' for Championship Fight or 'r' for Regular Fight: ")

if fight_type.lower() == 'c':
    print("\nChampionship Fight:")
    boxing_game(rounds=12)
elif fight_type.lower() == 'r':
    print("\nRegular Fight:")
    boxing_game(rounds=3)
else:
    print("Invalid choice. Please enter 'c' for Championship Fight or 'r' for Regular Fight.")
