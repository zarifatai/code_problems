class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        max_count = 0
        chars = []
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[j] not in chars:
                    chars.append(s[j])
                    count += 1
                else:
                    chars = []
                    break
                max_count = max(max_count, count)
        return max_count