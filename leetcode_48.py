from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                top_left = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left
            left += 1
            right -= 1

    def rotate_2(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(zip(*matrix[::-1]))
