from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for char, count in s_counter.items():
            if t_counter[char] != count:
                return False
        return True

    def is_anagram_2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(s)


s = Solution()
print(s.is_anagram("a", "ab"))
