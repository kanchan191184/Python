import random
import os

player_score = 0
cpu_hand = ''
cpu_score = 0

print("Welcome to the Rock Paper Scissors!")

while True:

    input("Press any key to continue....")

    #clearing the screen
    os.system('cls')

    player_hand = ''
    #loop for user input (player_hand)
    while player_hand != 'R' and player_hand != 'P' and player_hand != 'S':

        player_hand = input("Please select either: [R]ock, [P]aper, or [S]cissor\n").upper().strip()

        if player_hand == 'R':
            pass
        elif player_hand == 'P':
            pass
        elif player_hand == 'S':
            pass
        else:
            print("Invalid menu selection.")

    #get cpu_hand
    cpu_hand = random.choice(['R','S','P'])
    print("CPU Select:" + cpu_hand)

    # score the game
    if player_hand == cpu_hand:
        print("Draw")
    elif player_hand == 'R':
        if cpu_hand == 'P':
            print("CPU Wins")
            cpu_score = cpu_score + 1
        elif cpu_hand == 'S':
            print("Player Wins")
            player_score = player_score + 1 

    elif player_hand == 'P':
        if cpu_hand == 'R':
            print("Player Wins")
            player_score = player_score + 1
        elif cpu_hand == 'S':
            print("CPU Wins")
            cpu_score = cpu_score + 1

    elif player_hand == 'S':
        if cpu_hand == 'P':
            print("Player Wins")
            player_score = player_score + 1
        elif cpu_hand == 'R':
            print("CPU Wins")
            cpu_score = cpu_score + 1

    
    # print the score
    print("===Score====")
    print("CPU Score: " + str(cpu_score))
    print("Player Score: " + str(player_score))


