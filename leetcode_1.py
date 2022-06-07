from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for idx, num in enumerate(nums):
            match = target - num
            if match in ref:
                return [ref[match], idx]
            else:
                ref[num] = idx
