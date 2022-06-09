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
    
    def length_of_longest_substring_2(self, s: str) -> int:
        left = 0
        max_length = 0
        chars = set()

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1
            chars.add(char)
            max_length = max(max_length, right - left + 1)
        return max_length