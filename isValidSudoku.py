def isValidSudoku(board):
  '''
  Given an initial sudoku board with numbers as list of lists, find if it is valid or not
  Each internal list is one row of sudoku
  '''

  def _listCheck(numList):
    seen = set()
    for x in numList:
      if x in seen and x != ".": return False
      seen.add(x)
    return True

  for row in board:
    if _listCheck(row)==False:
      return False
      break

  for colIndex in range(9):
    col = []
    for rowIndex in range(9):
      col.append(board[rowIndex][colIndex])
    if _listCheck(col)==False:
      return False
      break

  for rowSet in range(3):
    board_sub = board[rowSet*3:(rowSet+1)*3]
    for index in range(3):
      grid = [board_sub[0][index*3], board_sub[0][index*3+1], board_sub[0][index*3+2],
              board_sub[1][index*3], board_sub[1][index*3+1], board_sub[1][index*3+2],
              board_sub[2][index*3], board_sub[2][index*3+1], board_sub[2][index*3+2]]
      if _listCheck(grid)==False:
        return False
        break

  return True
