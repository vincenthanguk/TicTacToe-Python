from tictactoemodules import display_board
from tictactoemodules import player_input
from tictactoemodules import place_marker
from tictactoemodules import win_check
from tictactoemodules import choose_first
from tictactoemodules import full_board_check
from tictactoemodules import player_choice
from tictactoemodules import random_choice
from tictactoemodules import replay
from tictactoemodules import cpu_get_move
import time

while True:

    theBoard = [' '] * 10
    player1marker, player2marker = player_input()
    turn = choose_first()
    print("\n\n~~ Welcome to TicTacToe! ~~")
    print("\n\nType '2' for Two Player Game")
    print("Type 'E' to play against easy CPU")
    print("Type 'random' to watch two easy CPUs play against each other")
    print("Type 'H' to play against hard CPU")
    print("Type 'XOXO' to watch two hard CPUs play against each other")
    play_game = input("\nMake your choice: ")
    print('\n'+turn + ' will go first.\n')
    time.sleep(0.5)
    print('\n'*10)
    print('Time for TicTacToe!!!\n\n')
    time.sleep(0.5)



    if play_game[0] == '2':
        humangame_on = True

        while humangame_on:
            if turn == 'Player 1':
                # Player 1's turn.

                print("\n")
                display_board(theBoard)
                print(f"\nYour turn, Player 1 ({player1marker})")
                position = player_choice(theBoard)
                place_marker(theBoard, player1marker, position)

                if win_check(theBoard, player1marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nCongratulations! Player 1 has won the game!')
                    humangame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!")
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player 2's turn.

                print("\n")
                display_board(theBoard)
                print(f"\nYour turn, Player 2({player2marker})")
                position = player_choice(theBoard)
                place_marker(theBoard, player2marker, position)

                if win_check(theBoard, player2marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nCongratulations! Player 2 has won the game!')
                    humangame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break
## Player vs. CPU

    if play_game[0].upper() == 'E':
        computergame_on = True
        while computergame_on:
            if turn == 'Player 1':
                # Player 1's turn.

                display_board(theBoard)
                print(f"\nYour turn, Player 1 ({player1marker})\n")
                position = player_choice(theBoard)
                place_marker(theBoard, player1marker, position)

                if win_check(theBoard, player1marker):
                    print("\n")
                    display_board(theBoard)
                    print('\nCongratulations! Player 1 has won the game!\n')
                    computergame_on = False
                else:
                    if full_board_check(theBoard):
                        print("\n")
                        display_board(theBoard)
                        print("\nThe game is a draw!\n")
                        break
                    else:
                        turn = 'Player 2'

            else:
                # computer's turn.
                print("\n")
                display_board(theBoard)
                print(f"\nYour turn, CPU ({player2marker})\n")
                # hier brauche ich jetzt den random placer
                time.sleep(1.5)
                print("\n...thinking...\n")
                time.sleep(1.5)
                position = random_choice(theBoard)
                place_marker(theBoard, player2marker, position)

                if win_check(theBoard, player2marker):
                    print("\n")
                    display_board(theBoard)
                    print('\nThe Computer has won the game!\n')
                    computergame_on = False
                else:
                    if full_board_check(theBoard):
                        print("\n")
                        display_board(theBoard)
                        print("\nThe game is a draw!\n")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

# CPU VS CPU RANDOM MATCH

    if play_game.upper() == 'RANDOM':
        cpuvscpugame_on = True
        while cpuvscpugame_on:
            if turn == 'Player 1':
                # Player 1's turn.

                display_board(theBoard)
                print(f"\nYour turn, CPU 1 ({player1marker})")
                time.sleep(1.5)
                print("\n...thinking...\n")
                time.sleep(1.5)
                position = random_choice(theBoard)
                place_marker(theBoard, player1marker, position)

                if win_check(theBoard, player1marker):
                    display_board(theBoard)
                    print('Congratulations! CPU 1 has won the game!')
                    cpuvscpugame_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 2'

            else:
                # computer's turn.

                display_board(theBoard)
                print(f"\nYour turn, CPU 2 ({player2marker})")
                time.sleep(1.5)
                print("\n...thinking...\n")
                time.sleep(1.5)
                # hier brauche ich jetzt den random placer

                position = random_choice(theBoard)
                place_marker(theBoard, player2marker, position)

                if win_check(theBoard, player2marker):
                    display_board(theBoard)
                    print('CPU 2 has won the game!')
                    cpuvscpugame_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

## Player vs. HARD CPU

    if play_game[0].upper() == 'H':
        hardcomputergame_on = True
        while hardcomputergame_on:
            if turn == 'Player 1':
                # Player 1's turn.

                print('\n')
                display_board(theBoard)
                print(f"\nYour turn, Player 1 ({player1marker})")
                print('\n')
                position = player_choice(theBoard)
                place_marker(theBoard, player1marker, position)

                if win_check(theBoard, player1marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nCongratulations! Player 1 has won the game!')
                    hardcomputergame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!")
                        break
                    else:
                        turn = 'Player 2'

            else:
                # computer's turn.
                print('\n')
                display_board(theBoard)
                print(f"\nYour turn, CPU ({player2marker})")
                time.sleep(1.5)
                print("\n...thinking...\n")
                time.sleep(1.5)
                position = cpu_get_move(theBoard,player2marker)

                place_marker(theBoard, player2marker, position)

                if win_check(theBoard, player2marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nThe Computer has won the game!')
                    hardcomputergame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!\n")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

# Hard CPU observer game

    if play_game[0].upper() == 'X':
        hardcomputerobsgame_on = True
        while hardcomputerobsgame_on:
            if turn == 'Player 1':
                # computer 1's turn.
                print('\n')
                display_board(theBoard)
                print(f"\nYour turn, CPU 1 ({player1marker})")

                time.sleep(1.5)
                print("\n...thinking...hard...\n")
                time.sleep(1.5)

                position = cpu_get_move(theBoard, player1marker)

                place_marker(theBoard, player1marker, position)

                if win_check(theBoard, player1marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nCPU 1 has won the game!')
                    hardcomputerobsgame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!\n")
                        break
                    else:
                        turn = 'Player 2'

            else:
                # computer 2's turn.
                print('\n')
                display_board(theBoard)
                print(f"\nYour turn, CPU 2 ({player2marker})")

                time.sleep(1.5)
                print("\n...thinking...hard...\n")
                time.sleep(1.5)

                position = cpu_get_move(theBoard,player2marker)

                place_marker(theBoard, player2marker, position)

                if win_check(theBoard, player2marker):
                    print('\n')
                    display_board(theBoard)
                    print('\nCPU 2 has won the game!')
                    hardcomputerobsgame_on = False
                else:
                    if full_board_check(theBoard):
                        print('\n')
                        display_board(theBoard)
                        print("\nThe game is a draw!\n")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break