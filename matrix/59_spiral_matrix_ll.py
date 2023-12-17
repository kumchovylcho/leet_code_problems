# https://leetcode.com/problems/spiral-matrix-ii/


from typing import List
from collections import deque


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = self.create_field(n)
        start_number = 2
        start_row, start_col = 0, 0
        matrix[start_row][start_col] = start_number - 1

        que = deque([
            lambda: self.set_to_right(matrix, start_row, start_col + 1, start_number),
            lambda: self.set_to_bottom(matrix, start_row + 1, start_col, start_number),
            lambda: self.set_to_left(matrix, start_row, start_col - 1, start_number),
            lambda: self.set_to_top(matrix, start_row - 1, start_col, start_number),
            ]
        )

        while self.neighbour_empty(start_row, start_col, matrix):
            execute_command = que[0]
            matrix, start_row, start_col, start_number = execute_command()
            que.rotate(1)

        return matrix

    def neighbour_empty(self, row, col, matrix):
        directions = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for x, y in directions:
            check_row, check_col = row + x, col + y

            if not self.valid_index(check_row, check_col, matrix):
                continue

            if self.can_place_number(check_row, check_col, matrix):
                return True

        return False

    def set_to_right(self, matrix, row: int, col: int, number: int):
        if not self.valid_index(row, col, matrix):
            return matrix, row, col - 1, number

        if not self.can_place_number(row, col, matrix):
            return matrix, row, col - 1, number

        matrix[row][col] = number
        return self.set_to_right(matrix, row, col + 1, number + 1)

    def set_to_bottom(self, matrix, row: int, col: int, number: int):
        if not self.valid_index(row, col, matrix):
            return matrix, row - 1, col, number

        if not self.can_place_number(row, col, matrix):
            return matrix, row - 1, col, number

        matrix[row][col] = number
        return self.set_to_bottom(matrix, row + 1, col, number + 1)

    def set_to_left(self, matrix, row: int, col: int, number: int):
        if not self.valid_index(row, col, matrix):
            return matrix, row, col + 1, number

        if not self.can_place_number(row, col, matrix):
            return matrix, row, col + 1, number

        matrix[row][col] = number
        return self.set_to_left(matrix, row, col - 1, number + 1)

    def set_to_top(self, matrix, row: int, col: int, number: int):
        if not self.valid_index(row, col, matrix):
            return matrix, row + 1, col, number

        if not self.can_place_number(row, col, matrix):
            return matrix, row + 1, col, number

        matrix[row][col] = number
        return self.set_to_top(matrix, row - 1, col, number + 1)

    def valid_index(self, row: int, col: int, matrix):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])

    def can_place_number(self, row: int, col: int, matrix):
        return matrix[row][col] == ""

    def create_field(self, n: int) -> List[List[str]]:
        matrix = []
        for row in range(n):
            matrix.append([""] * n)

        return matrix



n = 4
solution = Solution()
result = solution.generateMatrix(n)
print(result)
