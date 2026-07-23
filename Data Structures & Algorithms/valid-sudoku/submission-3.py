
# APPROACH: For a board to be valid, no digit can repeat within any
# row, column, or 3x3 box. So keep a set() for each of the 9 rows,
# 9 columns, and 9 boxes -> square_set is a 3x3 grid of sets (9 sets
# total), since rows//3 and cols//3 only ever produce 0, 1, or 2.
# Scan every filled cell once: if its digit is already in that cell's
# row/col/box set -> invalid, return False. Otherwise add it to all
# three sets and keep going.
# Box index trick: rows//3 and cols//3 map indices 0-8 down to 0-2,
# since rows/cols 0,1,2 -> box 0 | 3,4,5 -> box 1 | 6,7,8 -> box 2.
#
# HOW TO RESTART IF STUCK:
# 1. Ask: what are the "groups" that can't have duplicates? (row, col, box)
# 2. For each group type, set up one set per group (9 rows + 9 cols +
#    a 3x3 grid of box sets = 27 sets total).
# 3. Loop every cell once. Skip '.'. For filled cells, check membership
#    in the 3 relevant sets before adding.
# 4. The only tricky part is mapping (row, col) -> box index: use //3.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                cur_num = board[row][col]
                if cur_num == '.':
                    continue
                if (cur_num in row_set[row] or 
                 cur_num in col_set[col] or
                 cur_num in square_set[row//3][col//3]):
                 return False   
                row_set[row].add(cur_num) 
                col_set[col].add(cur_num)
                square_set[row//3][col//3].add(cur_num)

        return True         