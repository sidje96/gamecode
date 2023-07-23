import random

# In general, if you want to use global variables, it's best to define them somewhere at the top of your file.
# If the origin of a global variable is in a function, stuff tends to get messy.
# And since the variables are declared on a high level, they are still in scope when using them in a function, so no need for the global keyword here.
# Also it is common practice to write global vars in all caps. Using global variables to also write to is generally not great, as it can get messy in larger codebases, but that's a topic for another moment.
CURRENT_PLAYER = ""
CPU_NUM = 0
CURRENT_SCORE = 0
CURRENT_PLAYER = "Player 1"
CPU_OPTIONS = [1, random.randint(1, 10), 10, 9, 8, 7, 6, 5, 4, 3, 2]
PLAYER_AMOUNT = 0

def cpu():
    global CURRENT_SCORE
    if PLAYER_AMOUNT == "0":
        cpu_num = random.randint(1, 10)
        return cpu_num
    elif PLAYER_AMOUNT == "1":
        if CURRENT_SCORE % 11 == 1:
            cpu_num = CPU_OPTIONS[random.randint(1, 10)]
            return cpu_num
        elif CURRENT_SCORE == 0:
            cpu_num = CPU_OPTIONS[1]
            return cpu_num
        else:
            cpu_num = CPU_OPTIONS[CURRENT_SCORE % 11]
            return cpu_num
    else:
        cpu_num = CPU_OPTIONS[CURRENT_SCORE % 11]
        return cpu_num


def player():
    global CURRENT_PLAYER

    player_input = 0
    global CURRENT_SCORE

    while player_input < 1 or player_input > 10:
        if PLAYER_AMOUNT == "2":
            if CURRENT_PLAYER == "Player 1":
                print("\nIt is", CURRENT_PLAYER, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        CURRENT_SCORE += player_input
                    else:
                        return
                    print(
                        f"You picked: {player_input} current score = {CURRENT_SCORE}")
                    if CURRENT_SCORE >= 100:
                        return
                    else:
                        CURRENT_PLAYER = "Player 2"
                        continue
            else:
                print("\nIt is", CURRENT_PLAYER, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        CURRENT_SCORE += player_input
                    else:
                        return
                    print(
                        f"You picked: {player_input} current score = {CURRENT_SCORE}")
                    if CURRENT_SCORE >= 100:
                        return
                    else:
                        CURRENT_PLAYER = "Player 1"
                        continue

        elif PLAYER_AMOUNT == "3":
            if CURRENT_PLAYER == "Player 1":
                print("\nIt is", CURRENT_PLAYER, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        CURRENT_SCORE += player_input
                    else:
                        continue
                    print(
                        f"You picked: {player_input} current score = {CURRENT_SCORE}")
                    if CURRENT_SCORE >= 100:
                        return
                    else:
                        CURRENT_PLAYER = "Player 2"
                        continue

            elif CURRENT_PLAYER == "Player 2":
                print("\nIt is", CURRENT_PLAYER, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        CURRENT_SCORE += player_input
                    else:
                        continue
                    print(
                        f"You picked: {player_input} current score = {CURRENT_SCORE}")
                    if CURRENT_SCORE >= 100:
                        return
                    else:
                        CURRENT_PLAYER = "Player 3"
                        continue

            else:
                print("\nIt is", CURRENT_PLAYER, "'s turn")
                player_input = input("Pick a number from 1-10 ")
                if player_input.isdigit():
                    player_input = int(player_input)
                    if 0 < player_input <= 10:
                        CURRENT_SCORE += player_input
                    else:
                        continue
                    print(
                        f"You picked: {player_input} current score = {CURRENT_SCORE}")
                    if CURRENT_SCORE >= 100:
                        return
                    else:
                        CURRENT_PLAYER = "Player 1"
                        continue
        else:
            print("\nIt is", CURRENT_PLAYER, "'s turn")
            player_input = input("Pick a number from 1-10 ")
            if player_input.isdigit():
                player_input = int(player_input)
                if 0 < player_input <= 10:
                    CURRENT_SCORE += player_input
                else:
                    continue
                print(
                    f"You picked: {player_input} current score = {CURRENT_SCORE}")
                return check_win()


def check_win(): #It's always good to make function names as descriptive as possible. "check_win" might make it a bit more clear what this function does, rather than "gamestate".
    global CURRENT_SCORE
    if CURRENT_SCORE >= 100:
        return True
    else:
        return False


def gamecpu():
    global CURRENT_SCORE
    global CURRENT_PLAYER
    CURRENT_PLAYER = "Player 1"
    while CURRENT_SCORE < 100:
        cpu_num = cpu()
        CURRENT_SCORE += cpu_num
        print(
            f"\nThe CPU picked: {cpu_num} The current score = {CURRENT_SCORE}")
        if check_win():
            CURRENT_PLAYER = "CPU"
        else:
            player()

    if CURRENT_PLAYER == "Player 1":
        print(f"{CURRENT_PLAYER} won the game.")
    else:
        print(f"CPU won the game.")


#I've moved a bunch of logic into the "main" function.
# Earlier, there was some code running at the op of the file, then some functions were declared, and then it ran some more code.
# This way, your code has a very clear "entry point", or starting point, from where you can easily follow what it's running.
def main(): 
    global PLAYER_AMOUNT
    print("""
    The 100-game is played as follows:
    You pick a number from 1-10. It can't be less than 1
    or bigger than 10
    You and a CPU or second player take turns.
    The number you or the opponent picks, gets
    added to the total score.
    Whoever gets to 100 first wins the game.""")


    PLAYER_AMOUNT = input(
        """
    Do you wanna play against a CPU
    or against a friend?
    Type:
    0 for easy CPU
    1 for a more challenging experience against the CPU
    2 for 2 players
    3 for 3 players
    4 for perfect playing CPU\n""")

    
    p_a_check = ["0", "1"]

    if PLAYER_AMOUNT in p_a_check:
        start = input("Do you want to start? ").lower()
        if start == "yes":
            player()
        gamecpu()
    elif PLAYER_AMOUNT == "4":
        gamecpu()
    else:
        while not check_win():
            player()
        print(f"{CURRENT_PLAYER} won the game")

main() #So this is where we actually start running code