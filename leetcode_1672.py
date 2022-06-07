from typing import List


class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > max:
                max = wealth
        return max
