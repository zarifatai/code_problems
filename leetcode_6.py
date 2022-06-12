class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows > len(s):
            return s

        matrix = [""] * num_rows
        index, step = 0, 1

        for char in s:
            matrix[index] += char
            if index == 0:
                step = 1
            elif index == num_rows - 1:
                step = -1
            index += step
        return "".join(matrix)
