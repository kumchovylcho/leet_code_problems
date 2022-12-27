# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            cols = len(matrix[row])
            for col in range(cols):
                if matrix[row][col] == target:
                    return True
        return False