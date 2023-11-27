from typing import List, Tuple


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        updates = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]:
                    if self.check_live_neighbours(board, row, col, "two or three"):
                        continue

                    if self.check_live_neighbours(board, row, col, "less than two") or \
                        self.check_live_neighbours(board, row, col, "more than three"):
                        updates[row, col] = 0

                elif not board[row][col]:
                    if self.check_live_neighbours(board, row, col, "exactly three"):
                        updates[row, col] = 1

        for (row, col), value in updates.items():
            board[row][col] = value

    def check_live_neighbours(self, board: List[List[int]], row: int, col: int, neighbours: str) -> bool:
        bridge = {
            "less than two": lambda x: x < 2,
            "two or three": lambda x: x in [2, 3],
            "more than three": lambda x: x > 3,
            "exactly three": lambda x: x == 3
        }

        live_neighbours = 0
        for check_row, check_col in self.get_directions():
            look_row = row + check_row
            look_col = col + check_col

            if not self.valid_index(board, look_row, look_col):
                continue

            if board[look_row][look_col]:
                live_neighbours += 1

        return bridge[neighbours](live_neighbours)

    def valid_index(self, board: List[List[int]], row: int, col: int):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def get_directions(self) -> Tuple[Tuple[int, int]]:
        directions = (
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, -1),  # down-left
            (1, 1),   # down-right
            (-1, -1), # up-left
            (-1, 1),  # up-right
        )
        return directions


# board = [[1,1],[1,0]]
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

solution = Solution()
solution.gameOfLife(board)