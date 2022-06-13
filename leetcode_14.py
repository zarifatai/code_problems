from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest_str = min(strs, key=len)
        for idx, char in enumerate(shortest_str):
            for s in strs:
                if s[idx] != char:
                    return shortest_str[:idx]
        return shortest_str
