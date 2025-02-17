import random
from invalid_choice import InvalidChoice

def check_win_con(game_board, sym:str):
    """Checks to see if any win condition has been met"""
    wincon = [[0,1,2],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[0,3,6],[0,4,8],[2,4,6]]
    for con in wincon:
        count = 0
        for loc in con:
            if game_board[loc] == sym:
                count+=1
        if count == 3:
            print(f"{sym} won")
            return True

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def main():
    # Initialize the board with numbers 1 to 9
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(board)
    turns = 0

    while True:
        while True:
            try:
                user_choice = int(input("\nSelect your square: "))-1
                if board[user_choice] in ['X','O']:
                    raise InvalidChoice()
            except InvalidChoice:
                print("Please enter a free square")
            except ValueError:
                print("Invalid choice, please enter a value between 1 and 9")
            else:
                turns+=1
                break

        board[user_choice] = 'O'
        print_board(board)
        if check_win_con(board, 'O'):
            break

        if turns == 9:
            print('game over')
            break

        while True:
            try:
                comp_choice = int(random.choice(board))
                if board[comp_choice - 1] in ['X', 'O']:
                    raise InvalidChoice
            except ValueError:
                pass
            except InvalidChoice:
                pass
            else:
                turns += 1
                break

        print(f"\nComputer chose {comp_choice}\n")
        board[comp_choice - 1] = 'X'
        print_board(board)
        if check_win_con(board, 'X'):
            break





if __name__ =='__main__':
    main()
