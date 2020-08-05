import os
import sys
from platform import system
from random import randint

scheme = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def clear_screen():
    """Clear the screen"""
    if system().lower() == "linux" or system().lower() == "darwin":
        os.system("clear")
    elif system().lower() == "windows":
        os.system("cls")

def draw_scheme(scheme=scheme):
    """Draw tic tac toe scheme"""
    print("\t", scheme[0][0], "\t║\t", scheme[0][1], "\t║\t", scheme[0][2])
    print("════════════════╬═══════════════╬═════════════════")
    print("\t", scheme[1][0], "\t║\t", scheme[1][1], "\t║\t", scheme[1][2])
    print("════════════════╬═══════════════╬═════════════════")
    print("\t", scheme[2][0], "\t║\t", scheme[2][1], "\t║\t", scheme[2][2])


def play(player, symbol, scheme=scheme):
    """Allows the player to select a position"""
    while True:
        try:
            position = int(input(f'{player} ({symbol}) Enter the position: '))
            if position not in (1, 2, 3, 4, 5, 6, 7, 8, 9): raise ValueError
            if position in scheme[0] or position in scheme[1] or position in scheme[2]: pass
            else: raise ValueError
        except ValueError:
            clear_screen()
            print(f"{player} Enter a valid position..")
            draw_scheme()
        else:
            if 1 <= position <= 3: scheme[0][position-1] = symbol
            elif 4 <= position <= 6: scheme[1][position-4] = symbol
            elif 7 <= position <= 9: scheme[2][position-7] = symbol
            break

def check_win(name, symbol, scheme=scheme):
    """
    Check if a player has won otherwise report a tie
    """
    if (scheme[0][0] == symbol and scheme[0][1] == symbol and scheme[0][2] == symbol or
        scheme[1][0] == symbol and scheme[1][1] == symbol and scheme[1][2] == symbol or
        scheme[2][0] == symbol and scheme[2][1] == symbol and scheme[2][2] == symbol or
        scheme[0][0] == symbol and scheme[1][0] == symbol and scheme[2][0] == symbol or
        scheme[0][1] == symbol and scheme[1][1] == symbol and scheme[2][1] == symbol or
        scheme[0][2] == symbol and scheme[1][2] == symbol and scheme[2][2] == symbol or
        scheme[0][0] == symbol and scheme[1][1] == symbol and scheme[2][2] == symbol or
        scheme[0][2] == symbol and scheme[1][1] == symbol and scheme[2][0] == symbol):
        draw_scheme()
        print(f"{name} you won!")
        sys.exit() 
    elif (scheme[0][0] != 1 and scheme[0][1] != 2 and scheme[0][2] != 3 and
          scheme[1][0] != 4 and scheme[1][1] != 5 and scheme[1][2] != 6 and
          scheme[2][0] != 7 and scheme[2][1] != 8 and scheme[2][2] != 9):
          draw_scheme()
          print("Draw!")
          sys.exit()
        
def main():
    """main function"""
    print("Let's play!")
    player1 = input("Player1 Enter your name: ").strip().title()
    player2 = input("Player2 Enter your name: ").strip().title()
    players = ((player1,"X"),(player2,"O"))
    round = randint(0,1)
    print(f"{players[round][0]} starts...")
    while True:
        round %= 2
        draw_scheme()
        play(players[round][0],players[round][1])
        clear_screen()
        check_win(players[round][0],players[round][1])
        round += 1

if __name__ == '__main__':
    main()
