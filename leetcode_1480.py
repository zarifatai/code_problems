def runningSum(nums):
    return [sum(nums[: x + 1]) for x in range(len(nums))]
