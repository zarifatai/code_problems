from typing import List


class Solution:
    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        n = []
        for i, val in enumerate(mat):
            n.append((sum(val), i))
        sorted_n = sorted(n)
        _, res = list(zip(*sorted_n))
        return list(res)[:k]
