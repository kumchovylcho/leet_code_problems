# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1
        memo = {
            (rows, cols): 1
        }

        def get_unique_paths(row: int, col: int, obstacleGrid: List[List[int]]) -> int:
            if row == len(obstacleGrid) or col == len(obstacleGrid[row]) or obstacleGrid[row][col] == 1:
                return 0

            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = get_unique_paths(row + 1, col, obstacleGrid) + get_unique_paths(row, col + 1, obstacleGrid)

            return memo[(row, col)]

        return get_unique_paths(0, 0, obstacleGrid)


obstacleGrid = \
    [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],
     [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],
     [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
     [0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],
     [1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
     [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
     [0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
     [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
     [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
     [1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
     [0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],
     [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],
     [0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
     [0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
     [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],
     [1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
     [1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]

solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))
