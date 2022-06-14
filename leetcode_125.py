class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        mid_idx = (len(s) - 1) // 2
        right = mid_idx + 1

        if len(s) % 2 == 0:
            left = mid_idx
        else:
            left = mid_idx - 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True
