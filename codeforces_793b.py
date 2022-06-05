from functools import reduce

t = int(input())

for _ in range(t):
    permut_len = int(input())
    p_list = list(map(int, input().split(' ')))

    not_sorted = []
    for idx, val in enumerate(p_list):
        if val != idx:
            not_sorted.append(val)
    print(reduce(lambda x, y: x & y, not_sorted))

