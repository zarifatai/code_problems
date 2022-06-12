class Solution:
    def longest_palindrome(self, s: str) -> str:
        longest_length = 0
        longest_pal = ""

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest_length:
                    longest_length = right - left + 1
                    longest_pal = s[left : right + 1]
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest_length:
                    longest_length = right - left + 1
                    longest_pal = s[left : right + 1]
                left -= 1
                right += 1
        return longest_pal
