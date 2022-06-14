from typing import List
from collections import Counter


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


s = Solution()
print(s.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
