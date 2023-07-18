import random

print("""
The 100-game is played as follows:
You pick a number from 1-10. It can't be less than 1
or bigger than 10
You and a CPU or second player take turns.
The number you or the opponent picks, gets
added to the total score.
Whoever gets to 100 first wins the game.""")

global current_score
global current_player
global cpu_num
current_score = 0
current_player = "Player 1"


player_amount = input(
    """
Do you wanna play against a CPU
or against a friend?
Type:
0 for easy CPU
1 for a more challenging experience against the CPU
2 for 2 players
3 for 3 players
4 for perfect playing CPU\n""")
cpu_pick = [1, random.randint(1, 10), 10, 9, 8, 7, 6, 5, 4, 3, 2]

def cpu():
    global current_score
    if player_amount == "0":
        cpu_num = random.randint(1, 10)
        return cpu_num
    elif player_amount == "1":
        if current_score % 11 == 1:
            cpu_num = cpu_pick[random.randint(1, 10)]
            return cpu_num
        elif current_score == 0:
            cpu_num = cpu_pick[1]
            return cpu_num
        else:
            cpu_num = cpu_pick[current_score % 11]
            return cpu_num
    else:
        cpu_num = cpu_pick[current_score % 11]
        return cpu_num

def player():
    global current_player
    global current_score
    player_input = 0
    
    while player_input < 1 or player_input > 10:
        if player_amount == "2":
            if current_player == "Player 1":
                print("\nIt is", current_player, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        current_score += player_input
                    else:
                        return
                    print(f"You picked: {player_input} current score = {current_score}")
                    if current_score >= 100:
                        return
                    else:
                        current_player = "Player 2"
                        continue
            else:
                print("\nIt is", current_player, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        current_score += player_input
                    else:
                        return
                    print(f"You picked: {player_input} current score = {current_score}")
                    if current_score >= 100:
                        return
                    else:
                        current_player = "Player 1"
                        continue

        elif player_amount == "3":
            if current_player == "Player 1":
                print("\nIt is", current_player, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        current_score += player_input
                    else:
                        continue
                    print(f"You picked: {player_input} current score = {current_score}")
                    if current_score >= 100:
                        return
                    else:
                        current_player = "Player 2"
                        continue
                    
            elif current_player == "Player 2":
                print("\nIt is", current_player, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        current_score += player_input
                    else:
                        continue
                    print(f"You picked: {player_input} current score = {current_score}")
                    if current_score >= 100:
                        return
                    else:
                        current_player = "Player 3"
                        continue
                    
            else:
                print("\nIt is", current_player, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        current_score += player_input
                    else:
                        continue
                    print(f"You picked: {player_input} current score = {current_score}")
                    if current_score >= 100:
                        return
                    else:
                        current_player = "Player 1"
                        continue
        else:
            print("\nIt is", current_player, "'s turn")
            player_input = input("Pick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    current_score += player_input
                else:
                    continue
                print(f"You picked: {player_input} current score = {current_score}")
                return gamestate()

p_a_check = ["0", "1"]

def gamestate():
    global current_score
    if current_score >= 100:
        return True
    else:
        return False

def gamecpu():
    global current_player
    global current_score
    current_player = "Player 1"
    while current_score < 100:
        cpu_num = cpu()
        current_score += cpu_num
        print(f"\nThe CPU picked: {cpu_num} The current score = {current_score}")
        if gamestate():
            current_player = "CPU"
        else:
            player()

    if current_player == "Player 1":
        print(f"{current_player} won the game.")
    else:
        print(f"CPU won the game.")
    

if player_amount in p_a_check:
    start = input("Do you want to start? ").lower()
    if start == "yes":
        player()
    gamecpu()
elif player_amount == "4":
    gamecpu()
else:
    while not gamestate():
        player()
    print(f"{current_player} won the game")
    
