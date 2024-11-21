import random
import time

def delayed_print(message):
    time.sleep(1.5)
    print(message)

def winner(players_move, computers_move):
    who_wins = {"rock" : "scissors",
                "paper" : "rock",
                "scissors" : "paper",
                "fire" : ["paper", "scissors"],
                "water" : ["fire", "rock"]}
    
    if computers_move in who_wins[players_move]:
        return "player"
    elif computers_move == players_move:
        return "draw"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors, Water, Fire! Prepare to meet your fate...")
    print("---------------------------------------------------------------------------")

    players_name = input("Player's name:")
    
    delayed_print(f"Ready to play {players_name}?")

    player_score = 0
    computer_score = 0
    
    while True:
        choices = ["rock", "paper", "scissors", "water", "fire"]

        players_move = input("Rock, paper, scissors, water, or fire? ").lower()
        print("------------------------------------------------------------")

        if players_move not in choices:
            delayed_print("Invalid choice. Try again")
            continue

        computers_move = random.choice(choices)

        delayed_print(f"{players_name}'s choice: {players_move} vs Computer's choice: {computers_move}")

        game_result = winner(players_move, computers_move)

        if game_result == "player":
            delayed_print(f"{players_name} wins!!!!!!")
            player_score += 1 
        elif game_result == "draw":
            delayed_print("It's a draw. Try again")
            continue
        else:
            delayed_print("Computer wins!!!!!!")
            computer_score += 1

        delayed_print(f"Current score: {players_name} {player_score} - {computer_score} Computer")

        next_round = input("Want to play again? yes or no: ").lower()
        if next_round == "no":
            print("Thanks for playing")
            break

play_game()