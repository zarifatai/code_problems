def pivotIndex(nums):
    left, right = 0, sum(nums)

    for idx, n in enumerate(nums):
        right -= n
        if left == right:
            return idx
        left += n
    return -1
