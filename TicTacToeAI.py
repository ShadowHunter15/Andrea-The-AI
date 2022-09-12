import random
def wincheck(board):
        score = {
            "O": 1,
            "X": -1
        }
        for mark in ["O", "X"]:
            if ((board[0]==mark and board[1]== mark and board[2]==mark )or
                (board[3]==mark and board[4]==mark and board[5]==mark )or
                (board[6]==mark and board[7]==mark and board[8]==mark )or
                (board[0]==mark and board[3]==mark and board[6]== mark )or
                (board[1]==mark and board[4]==mark and board[7]==mark )or
                (board[2]==mark and board[5]==mark and board[8]==mark )or
                (board[0]==mark and board[4]==mark and board[8]==mark )or
                (board[2]==mark and board[4]==mark and board[6]==mark )):
                    return score[mark]
        for i in ["1","2","3","4","5","6","7","8","9"]:
            if i in board:
                break
            else:
                if i == "9":
                    return 0
depth = [0]
def bestMove(board):
    if depth[0] == 1:
        return random.choice([i+1 for i in range(len(board)) if board[i] not in ["X", "O"]])
    best = float("inf")
    move = 0
    if board.count("X") == 0 and board.count("O") == 0:
        return 5
    for i in range(len(board)):
        if board[i] not in ["X", "O"]:
            board[i] = "X"
            Try = findBestMove(board, 1, depth[0])
            if Try < best:
                best = Try
                move = i
            board[i] = str(i+1)
    return move+1
def findBestMove(board, maximizing, depth):
    if wincheck(board) is not None:
        return wincheck(board)
    if depth > 0:
        depth -= 1
        if maximizing == 1:
            best = float("-inf")
            for i in range(len(board)):
                if board[i] not in ["X", "O"]:
                    board[i] = "O"
                    Try = findBestMove(board, 0, depth)
                    board[i] = str(i+1)
                    best = max(best, Try)
            return best
        if maximizing == 0:
            best = float("inf")
            for i in range(len(board)):
                if board[i] not in ["X", "O"]:
                    board[i] = "X"
                    Try = findBestMove(board, 1, depth)
                    board[i] = str(i+1)
                    best = min(best, Try)
            return best
    else:
        return 0
