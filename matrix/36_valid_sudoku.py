# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for box_row in range(0, 9, 3):
            for box in range(0, 9, 3):
                if not self.box_is_valid(board, box_row, box):
                    return False

            for row in range(box_row, box_row + 3):
                if not self.row_is_valid(board[row]) or \
                    not self.row_is_valid(self.col_to_row(board, 0, 9, row)):
                    return False

        return True

    def box_is_valid(self, board: List[List[str]], box_row, box: int) -> bool:
        box_in_row = []
        for row_in_box in range(3):
            whole_row = board[box_row + row_in_box]
            symbols_in_row_in_box = whole_row[box: box + 3]
            box_in_row.extend(symbols_in_row_in_box)

        return self.row_is_valid(box_in_row)

    def row_is_valid(self, current_row: list) -> bool:
        uniques = []

        for symbol in current_row:
            if symbol == ".":
                continue

            if symbol in uniques:
                return False

            uniques.append(symbol)

        return True

    def col_to_row(self, board: List[List[str]], row: int, how_many_rows: int, col: int):
        result = []
        for curr_row in range(row, how_many_rows):
            result.append(board[curr_row][col])

        return result

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board3 = \
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]

solution = Solution()
solution.isValidSudoku(board)