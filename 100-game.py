import random

print("""
The 100-game is played as follows:
You pick a number from 1-10. It can't be less than 1
or bigger than 10
You and a CPU or second player take turns.
Whoever gets to 100 first wins the game.""")




def easy_cpu():
    current_score = 0
    current_player = "CPU"
    while current_score < 100:
        if current_player == "CPU":
            cpu_num = random.randint(1, 10)
            current_score += cpu_num
            print(f"\nThe cpu picked: {cpu_num}. current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "Player 1"
        else:
            player_input = input("\nPick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    current_score += player_input
                else:
                    continue
            else:
                continue
            print(f"You picked: {player_input} current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "CPU"
    if current_player == "Player 1":
        print(f"Congratulations! {current_player} won the game.")
    else:
        print("Unfortunately, you lost the game from the CPU")
            
def hard_cpu():
    current_score = 0
    current_player = "CPU"
    while current_score < 100:
        if current_player == "CPU":
            if current_score % 11 == 1:
                cpu_num = random.randint(1, 10)
            else:
                helper_dig = [1, 1]
                for i in range(2,11):
                    helper_dig.insert(2, i)
                cpu_num = helper_dig[current_score % 11]
            current_score += cpu_num
            print(f"\nThe cpu picked: {cpu_num}. current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "Player 1"
        else:
            player_input = input("\nPick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    current_score += player_input
                else:
                    continue
            else:
                continue
            print(f"You picked: {player_input} current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "CPU"
    if current_player == "Player 1":
        print(f"Congratulations! {current_player} won the game.")
    else:
        print("Unfortunately, you lost the game from the CPU")

def PVP():
    current_score = 0
    current_player = "Player 2"
    while current_score < 100:
        if current_player == "Player 2":
            print("\nIt is", current_player, "'s turn.")
            player_input = input("Pick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    current_score += player_input
                else:
                    continue
            else:
                continue
            print(f"You picked: {player_input} current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "Player 1"
        else:
            print("\nIt is", current_player, "'s turn")
            player_input = input("Pick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    current_score += player_input
                else:
                    continue
            else:
                continue
            print(f"You picked: {player_input} current score = {current_score}")
            if current_score >= 100:
                continue
            else:
                current_player = "Player 2"
    if current_player == "Player 1":
        print(f"Congratulations! {current_player} won the game.")
    else:
        print(f"Congratulations! {current_player} won the game.")


while True:
    player_amount = input(
    """
Do you wanna play against a CPU
or against a friend?
Type:
0 for easy CPU
1 for a more challenging experience against the CPU (You can't win)
2 for 2 players \n""")



    if player_amount == "0":
        easy_cpu()
        break
    elif player_amount == "1":
        hard_cpu()
        break
    elif player_amount == "2":
        PVP()
        break
    else:
        continue

