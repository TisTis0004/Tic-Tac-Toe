import random,time
from art import logo

def printBoard():
    b = f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
"""
    print(b)

board = [[1,2,3],[4,5,6],[7,8,9]]

moves = {
    1:[0,0],
    2:[0,1],
    3:[0,2],
    4:[1,0],
    5:[1,1],
    6:[1,2],
    7:[2,0],
    8:[2,1],
    9:[2,2],
}

wins = {
    0:[[0,0],[0,1],[0,2]],
    1:[[1,0],[1,1],[1,2]],
    2:[[2,0],[2,1],[2,2]],
    3:[[0,0],[1,0],[2,0]],
    4:[[0,1],[1,1],[2,1]],
    5:[[0,2],[1,2],[2,2]],
    6:[[0,0],[1,1],[2,2]],
    7:[[0,2],[1,1],[2,0]],
}

def takeMove():
    """Takes the user's move as an input(1-9), returns the position as a list."""
    while True:
        move = int(input("Enter your move(1-9): "))
        if moves[move] not in checkEmpty():
            print("This position is occupied.")
        elif move >= 1 and move <= 9:
            break
        print("Please enter a valid move(1-9).")
    return moves[move]


def checkEmpty():
    """Checks for the empty positions on the board,
      returns a list of lists each list is a pair of positions."""
    available_positions = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ["X","O"]:
                available_positions.append([r,c])
    return available_positions


def generateMove():
    """Generates a random position for a the computer's move, returns the position as a list."""
    while True:
        move = [random.randint(0,3),random.randint(0,3)]
        if move in checkEmpty():
            break
    return move


def updateBoard(pos,symbol):
    """Updates the board symboles from the numbers to the players symboles."""
    board[pos[0]][pos[1]] = symbol


def checkWinner(symbol):
    """Checks for the winner, returns True if the symbol(player) sent as a parameter is the winner,
      False otherwise."""
    for win in wins:
        cnt = 0
        for pos in wins[win]:
            if board[pos[0]][pos[1]] == symbol:
                cnt += 1
            if cnt == 3:
                return True
    return False


#Main function
if __name__ == "__main__":
    print(logo)
    printBoard()
    winner = None
    while True:
        human = takeMove()
        updateBoard(human,"O")
        printBoard()
        if checkWinner("O"):
            winner = "O"
            break
        if checkEmpty() == []:
            break
        computer = generateMove()
        updateBoard(computer,"X")
        print("computer is thinking 🤔 ...")
        time.sleep(1.5)
        printBoard()
        if checkWinner("X"):
            winner = "X"
            break
    if winner == "O":
        print("Congratulations you've beaten the computer 🥳.")
    elif winner == "X":
        print("You lost. The AI will take your job ☹️.")
    else:
        print("Tie 🤝. You and AI are friends now 😊.")