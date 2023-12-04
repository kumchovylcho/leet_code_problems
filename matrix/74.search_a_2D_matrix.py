# https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1] and target in row:
                return True

        return False




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

solution = Solution()
result = solution.searchMatrix(matrix, target)
print(result)

################################################################################################


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for row in range(len(matrix)):
#             cols = len(matrix[row])
#             for col in range(cols):
#                 if matrix[row][col] == target:
#                     return True
#         return False