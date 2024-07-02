def nqueens(board, row):
    global c
    # base case
    if row == len(board):
        c += 1
        printboard(board)
        return

    # column
    for j in range(len(board)):
        if issafe(board, row, j):
            board[row][j] = 'Q'
            nqueens(board, row + 1)
            board[row][j] = 'X'


def issafe(board, row, col):
    # vertical up
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False

    # up left
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # up right
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 'Q':
            return False

    return True


def printboard(board):
    global c
    print(f"----SOLUTION {c} ----")
    for row in board:
        print(' '.join(row))
    print()


if __name__ == "__main__":
    n=int(input("Enter the number of queens:"))
    if n >= 4:
        c = 0
        board = [['X' for _ in range(n)] for _ in range(n)]
        nqueens(board, 0)
        print(f"Total solutions = {c}")
    else:
        print("No solution")