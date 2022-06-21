from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        new_left, new_right = new_interval

        res = []
        for i, (curr_left, curr_right) in enumerate(intervals):
            if new_right < curr_left:
                res.append([new_left, new_right])
                return res + intervals[i:]
            if new_left > curr_right:
                res.append([curr_left, curr_right])
            else:
                new_left = min(curr_left, new_left)
                new_right = max(curr_right, new_right)
        return res + [[new_left, new_right]]
