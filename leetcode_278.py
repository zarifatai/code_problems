def first_bad_version(n):
    left = 0
    right = n

    while left < right:
        mid = left + (right - left) // 2

        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left
