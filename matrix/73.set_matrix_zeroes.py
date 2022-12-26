# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def find_zeroes():
            zero_pos = []
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] == 0:
                        zero_pos.append([row, col])
            return zero_pos

        def apply_zeroes(row, col):
            for c_row, c_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                m_row, m_col = row, col
                for direction in range(len(matrix) + len(matrix[row])):
                    m_row, m_col = m_row + c_row, m_col + c_col
                    if check_index(m_row, m_col):
                        matrix[m_row][m_col] = 0
                        continue
                    break

        def check_index(row, col):
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
                return True

        all_zeroes = find_zeroes()
        for z_row, z_col in all_zeroes:
            apply_zeroes(z_row, z_col)
