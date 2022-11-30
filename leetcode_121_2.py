def max_profit(prices):
    max_profit = 0
    left_idx = 0

    for right_idx in range(len(prices)):
        if prices[right_idx] < prices[left_idx]:
            left_idx = right_idx
        max_profit = max(max_profit, prices[right_idx] - prices[left_idx])
    return max_profit
