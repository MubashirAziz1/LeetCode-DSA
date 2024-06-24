class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

      # Validate the Rows
      for i in range(9):
        dupl = set()
        for j in range(9):
            if board[i][j] in dupl:
                return False
            elif board[i][j] == '.':
                continue
            else:
                dupl.add(board[i][j])
    
      # Validate the Columns
      for i in range(9):
          dupl = set()
          for j in range(9):
              if board[j][i] in dupl:
                  return False
              elif board[j][i] == '.':
                  continue
              else:
                  dupl.add(board[j][i])

      # Starting points for each 3x3 sub-boxes.
      start_points = [[0,0],[0,3],[0,6],
                      [3,0],[3,3],[3,6],
                      [6,0],[6,3],[6,6]]

      #Validate each sub-box 
      for rows, columns in start_points:
          for i in range(rows):
              dupl = set()
              for b1 in range(columns):
                  if board[rows][columns] in dupl:
                      return False
                  elif board[rows][columns] == '.':
                      continue
                  else:
                      dupl.add(board[rows][columns])
      return True
                
    
