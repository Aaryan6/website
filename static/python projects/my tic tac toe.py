print("***** Tic Tac Toe *****")

def game():
    board = {0:' ',1:' ',2:' ',
             3:' ',4:' ',5:' ',
             6:' ',7:' ',8:' '}
    def display_board():
        print()
        print(board[0]+' | '+board[1]+' | '+board[2])
        print('---------')
        print(board[3]+' | '+board[4]+' | '+board[5])
        print('---------')
        print(board[6]+' | '+board[7]+' | '+board[8])

    display_board()

    def tie():
        if count == 8:
            print("\nIt's a Tie!")

    turn = 'O'
    count = 0


    while count<9:
        # change turn
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'

        # user input
        move = int(input("Enter here : "))
        if board[move - 1] == ' ':
            board[move - 1] = turn
        else:
            print("You already entered input")
            continue

        # board
        display_board()

        # ---------row--------------
        if board[0] == board[1] == board[2] and board[0] == board[1] == board[2] != ' ':
            print(f"\n{board[0]} is  win")
            break
        elif board[3] == board[4] == board[5] and board[3] == board[4] == board[5] != ' ':
            print(f"\n{board[3]} is  win")
            break
        elif board[6] == board[7] == board[8] and board[6] == board[7] == board[8] != ' ':
            print(f"\n{board[6]} is  win")
            break
        # ---------column--------------
        elif board[0] == board[3] == board[6] and board[0] == board[3] == board[6] != ' ':
            print(f"\n{board[0]} is  win")
            break
        elif board[1] == board[4] == board[7] and board[1] == board[4] == board[7] != ' ':
            print(f"\n{board[1]} is  win")
            break
        elif board[2] == board[5] == board[8] and board[2] == board[5] == board[8] != ' ':
            print(f"\n{board[2]} is  win")
            break
        # --------------cross------------
        elif board[0] == board[4] == board[8] and board[0] == board[4] == board[8] != ' ':
            print(f"\n{board[0]} is  win")
            break
        elif board[2] == board[4] == board[6] and board[2] == board[4] == board[6] != ' ':
            print(f"\n{board[2]} is  win")
            break
        # check tie
        tie()
        count += 1

if __name__ == '__main__':
    game()
