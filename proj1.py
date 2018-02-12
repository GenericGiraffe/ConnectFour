# File: proj1.py
# Author: Blake Lewis
# Date: 11/16/16
# Description: This program is a simple connect four game

EMPTY = "_"
PLAYER_1 = "x"
PLAYER_2 = "o"

# emptyBoard() creates a blank connect four board
# input: dimensions of board
# output: the board
def emptyBoard():
    board = []
    # asks for the rows of the board
    rows = int(input("Please choose the number of rows: \nPlease enter a number greater than or equal to 5: "))
    while rows < 5:
        rows = int(input("Please choose the number of rows: \nPlease enter a number greater than or equal to 5: "))
    #asks for the columns of the board
    columns = int(input("Please choose the number of columns: \nPlease enter a number greater than or equal to 5: "))
    while columns < 5:
        columns = int(input("Please choose the number of columns: \nPlease enter a number greater than or equal to 5: "))
    # creates the board using the previous inputs for columns and rows
    board = [[EMPTY for c in range(columns)] for r in range(rows)]
    return board

# printBoard() takes the current board and prints it for the users
# input: board
# output: prints board    
def printBoard(board):
    # Puts a space in between the underscores
    for row in board:
        print(" ".join(row))
    return board

def main():
    gameLoad = ""
    print("Welcome to Connect Four!")
    print("This game is for two players")
    # Decides whether a user wants to load a game or not.
    while gameLoad != "y" and gameLoad != "n":
        gameLoad = input("Would you like to load a game (y/n)? ")
    if gameLoad == "y":
        board = load()
    elif gameLoad == "n":
        board = emptyBoard()
    printBoard(board)
    gamePlay(board)
    

# save() saves the current board to a file named by the user
# input: file name and board
# output: save file
def save(board):
    boardSave = ""
    lenRow = len(board)
    lenCol = len(board[0])
    userFile = input("What game file would you like to save to? ")
    myFile = open(userFile, "w")
    # Iterates through the 2D array and converts into a string
    for r in range(lenRow):
        for c in range(lenCol):
            boardSave += board[r][c]
        boardSave += "\n"
    myFile.write(boardSave)
    myFile.close
    print("File saved")
    
# load(): loads a board from a save file
# input: file name
# output: board
def load():
    userFile = input("What game file would you like to load from? ")
    myFile = open(userFile, "r")
    board = myFile.readlines()
    # This makes the list into one line
    board = [line.strip("\n") for line in board]
    # This separates the indices in the list into single element sublists
    board = [line.split(",") for line in board]
    # This turns the single element sublists into lists of the single element's characters
    board = [list(' '.join(board[i])) for i in range(len(board))]
    return board    

# gamePlay performs the logic for the board
# input: player choices
# output: board and gameplay
def gamePlay(board):
    choice = ""
    player = 0
    i = 1
    winner = False
    draw = False
    p1Win = False
    p2Win = False
    full = False
    # This loop runs until one of the player wins or there is a draw
    while winner != True:
        # This determines if there is a draw
        if draw == True:
            winner = True
            print("It's a draw!")
        # This determines if Player 1 wins
        elif p1Win == True:
            winner = True
            print("Player 1 is victorious!")
        # This determines if Player 2 wins
        elif p2Win == True:
            winner = True
            print("Player 2 is victorious!")
        # This decides if it is Player 1's turn
        elif player % 2 == 0:
            choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            if choice == "s":
                save(board)
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            # Input Validation
            while (int(choice) < 1 or int(choice) > len(board[0])):
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")

            if choice == "s":
                save(board)
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            # Moves up the column if the slot is valid
            while (board[len(board)-i][int(choice) - 1] != EMPTY):
                if board[0][int(choice) - 1] != EMPTY:
                    choice = input("That column is full.\nPlease choose a column to place your piece in (1 - "+str(len(board[0]))+") or s to save: ")
                    if choice == "s":
                        save(board)
                        choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
                else:
                    i += 1
            if choice == "s":
                save(board)
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")

            # Puts a x if the slot is valid
            board[len(board)-i][int(choice) - 1] = PLAYER_1
            printBoard(board)
            player += 1
            i = 1
            draw = drawGame(board)
            p1Win = player1Win(board)
            
        # Determines if it is Player 2's turn
        elif player % 2 != 0:
            choice = input("Player 2 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            if choice == "s":
                save(board)
                choice = input("Player 2 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            # Input Validation
            while (int(choice) < 1 or int(choice) > len(board[0])):
                choice = input("Player 2 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")

            if choice == "s":
                save(board)
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            # Determines if the slot is valid
            while (board[len(board)-i][int(choice) - 1] != EMPTY):
                if board[0][int(choice) - 1] != EMPTY:
                    choice = input("That column is full.\nPlease choose a column to place your piece in (1 - "+str(len(board[0]))+") or s to save: ")
                    if choice == "s":
                        save(board)
                        choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
                else:
                    i += 1
            if choice == "s":
                save(board)
                choice = input("Player 1 what is your choice? \nPlease choose a column to place your piece in (1 - " +str(len(board[0]))+") or s to save: ")
            # puts an o if the slot is valid
            board[len(board)-i][int(choice) - 1] = PLAYER_2
            printBoard(board)
            player += 1
            i = 1
            draw = drawGame(board)
            p2Win = player2Win(board)
    playAgain() 
    
    

# playAgain() determines if the player wants to restart the game
# input: y or n
# output: restarts gamePlay()
def playAgain():
    play = input("Would you like to play again (y/n)? ")
    while play != "y" and play != "n":
        play = input("Would you like to play again (y/n)? ")
    if play == "y":
        board = emptyBoard()
        printBoard(board)
        gamePlay(board)
        winner = False
        
        
    
# fullCol() determines whether a column is full or not
# input: board/column
# output: boolean
def fullCol(board, choice):
    if board[0][int(choice) - 1] != EMPTY:
        choice = input("That column is full.\nPlease choose a column to place your piece in (1 - "+str(len(board[0]))+") or s to save: ")
        
    
# drawGame() determines whether or not the game is a draw
# input: board
# output: boolean
def drawGame(board):
    # Determines if every slot is filled
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == EMPTY:
                return False
    return True

# player1Win() determines whether or not player 1 has won
# input: board
# output: boolean
def player1Win(board):
    # checks board for horizontal victory
    for r in range(len(board) - 3):
        for c in range(len(board[0])):
            if board[r][c] == PLAYER_1 and board[r + 1][c] == PLAYER_1 and board[r + 2][c] == PLAYER_1 and board[r + 3][c] == PLAYER_1:
                return True
    
    # checks board for vertical victory
    for r in range(len(board)):
        for c in range(len(board[0]) - 3):
            if board[r][c] == PLAYER_1 and board[r][c + 1] == PLAYER_1 and board[r][c + 2] == PLAYER_1 and board[r][c + 3] == PLAYER_1:
                return True

    # checks board for diagonal victory from top left to bottom right
    for r in range(len(board) - 3):
        for c in range(len(board[0]) - 3):
            if board[r][c] == PLAYER_1 and board[r + 1][c + 1] == PLAYER_1 and board[r + 2][c + 2] == PLAYER_1 and board[r + 3][c + 3] == PLAYER_1:
                return True

    # checks board for diagonal victory from bottom left to top right
    for r in range(len(board)-3):
        for c in range(3, len(board[0])):
            if board[r][c] == PLAYER_1 and board[r + 1][c - 1] == PLAYER_1 and board[r + 2][c - 2] == PLAYER_1 and board[r + 3][c - 3] == PLAYER_1:
                return True
    
    return False
               
            
            
# player2Win() determines whether or not player 2 has won
# input: board
# output: boolean
def player2Win(board):
    # checks board for horizontal victory
    for r in range(len(board) - 3):
        for c in range(len(board[0])):
            if board[r][c] == PLAYER_2 and board[r + 1][c] == PLAYER_2 and board[r + 2][c] == PLAYER_2 and board[r + 3][c] == PLAYER_2:
                return True
    
    # checks board for vertical victory
    for r in range(len(board)):
        for c in range(len(board[0]) - 3):
            if board[r][c] == PLAYER_2 and board[r][c + 1] == PLAYER_2 and board[r][c + 2] == PLAYER_2 and board[r][c + 3] == PLAYER_2:
                return True
    
    # checks board for diagonal victory from top left to bottom right
    for r in range(len(board) - 3):
        for c in range(len(board[0]) - 3):
            if board[r][c] == PLAYER_2 and board[r + 1][c + 1] == PLAYER_2 and board[r + 2][c + 2] == PLAYER_2 and board[r + 3][c + 3] == PLAYER_2:
                return True
    
    # checks board for diagonal victory from bottom left to top right
    for r in range(len(board)-3):
        for c in range(3, len(board[0])):
            if board[r][c] == PLAYER_2 and board[r + 1][c - 1] == PLAYER_2 and board[r + 2][c - 2] == PLAYER_2 and board[r + 3][c - 3] == PLAYER_2:
                return True
    
    return False

    
            
            
main()  
