import numpy as np


def isValidSudoku(board):
    """
    Given an initial sudoku board with numbers as list of lists, find if it is valid or not
    Each internal list is one row of sudoku
    """
    board = np.array(board)

    def _listCheck(numList):
        seen = set()
        for x in numList:
            if x in seen and x != ".":
                return False
            seen.add(x)
        return True

    for i in range(board.shape[0]):
        if not _listCheck(board[i].tolist()):
            return False
            break

    for i in range(board.shape[0]):
        if not _listCheck(board[:, i].tolist()):
            print("col fail", i)
            return False
            break

    for i in range(3):
        for j in range(3):
            if not _listCheck(board[i * 3:i * 3 + 3, j * 3:j * 3 + 3].flatten().tolist()):
                print("grid fail")
                return False
                break

    return True
