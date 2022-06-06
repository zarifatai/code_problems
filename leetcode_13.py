class Solution:
    def __init__(self):
        self.symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.subtractions = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    def roman_to_int(self, s: str) -> int:
        s = s.upper()
        res = 0
        for sub, value in self.subtractions.items():
            if sub in s:
                res += value
                s = s.replace(sub, "")
        for char in s:
            res += self.symbols[char]
        return res

