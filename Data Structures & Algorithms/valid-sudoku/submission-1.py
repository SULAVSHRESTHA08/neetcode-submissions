class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        square_set = [[set() for _ in range(9)] for _ in range (9)]

        for rows in range(9):
            for cols in range(9):
                if board[rows][cols] == '.':
                    continue 
                if(board[rows][cols] in row_set[rows] or 
                 board[rows][cols] in column_set[cols] or
                 board[rows][cols] in square_set[rows//3][cols//3]):
                  return False
                row_set[rows].add(board[rows][cols]) 
                column_set[cols].add(board[rows][cols]) 
                square_set[rows//3][cols//3].add(board[rows][cols]) 
        return True