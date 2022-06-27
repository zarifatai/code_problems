class Solution:
    def reverse_bits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            bit = n % 2
            res += bit
            n = n >> 1
        return res
