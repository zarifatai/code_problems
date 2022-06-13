class Solution:
    def is_palindrome(self, x: int) -> bool:
        x = str(x)
        mid_idx = (len(x) - 1) // 2
        left = mid_idx - 1

        if len(x) % 2 != 0:
            right = mid_idx + 1
        else:
            if x[mid_idx] != x[mid_idx + 1]:
                return False
            right = mid_idx + 2

        while left >= 0 and right < len(x):
            if x[left] == x[right]:
                left -= 1
                right += 1
            else:
                return False
        return True
