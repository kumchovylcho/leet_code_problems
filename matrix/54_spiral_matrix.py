from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        row, col = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        output = []

        while len(visited) != len(matrix) * len(matrix[0]):
            current_direction = directions.pop(0)
            directions.append(current_direction)

            while self.valid_index(matrix, row, col):
                number = matrix[row][col]

                curr_spot = tuple((row, col))
                if curr_spot in visited:
                    break

                visited.add(curr_spot)
                output.append(number)

                row += current_direction[0]
                col += current_direction[1]

            # move back if you went outside of matrix or already been there
            row -= current_direction[0]
            col -= current_direction[1]

            # prepare position for next direction, if we dont do that, then we will loop forever, since the spot is always visited
            next_row, next_col = directions[0]
            row += next_row
            col += next_col

        return output

    def valid_index(self, matrix: List[List[int]], row: int, col: int):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])


matrix = [[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]

solution = Solution()
result = solution.spiralOrder(matrix)
print(result)
