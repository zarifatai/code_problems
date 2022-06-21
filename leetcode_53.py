from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum
