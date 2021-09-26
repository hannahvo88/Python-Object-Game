
import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")


# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

board = gameboard.GameBoard()
played=player.Player(3,2)
while True:
    try:
        board.printBoard(played.rowPosition, played.columnPosition)
        selection = input("Make a move: ")
        
        
        # TODO
        # Move the player through the board
        
        if selection == "w":
            if board.checkMove(played.rowPosition -1, played.columnPosition):
                played.moveUp()
                board.printBoard(played.rowPosition, played.columnPosition)
        elif selection == "s":
            if board.checkMove(played.rowPosition +1, played.columnPosition):
                played.moveDown()
                board.printBoard(played.rowPosition, played.columnPosition)
        elif selection == "a":
            if board.checkMove(played.rowPosition, played.columnPosition -1):
                played.moveLeft()
                board.printBoard(played.rowPosition, played.columnPosition)
        elif selection == "d":
            if board.checkMove(played.rowPosition, played.columnPosition +1):
                played.moveRight()
                board.printBoard(played.rowPosition, played.columnPosition)
        else:
            print("Wrong move key. Please try again!")
            print("To move up: w")
            print("To move down: s")
            print("To move left: a")
            print("To move right: d")
            print("-----------------------------")  

    except ValueError:
        print("Sorry, I didn't understand that.")
        continue


    # Check if the player has won, if so print a message and break the loop!
    if board.checkWinner(played.rowPosition, played.columnPosition):
        print("You are the winner!")
        newstart = input("Do you want Start again? then click y, if Not click other key ")
        if newstart == "y":
            played=player.Player(3,2)
            board.printBoard(played.rowPosition, played.columnPosition)
            continue
        else:
            break
    else:
        continue

