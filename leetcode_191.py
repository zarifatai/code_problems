class Solution:
    def hamming_weight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
