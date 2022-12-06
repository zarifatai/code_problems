from collections import Counter


def longest_palindrome(s):
    c = Counter(s)
    chars_left = sum(c.values())

    if len(c) == 1:
        return len(s)

    length = 0
    while chars_left > 0:
        for key, val in c.items():
            if val >= 2:
                if val % 2 != 0:
                    val = val - 1
                length += val
                chars_left -= val
        break
    if chars_left == 0:
        return length
    else:
        return length + 1
    





    

