t = int(input())

for _ in range(t):
    count = 1
    n_char = int(input())
    string = input()

    mid = len(string) // 2

    walk = mid - 1
    while walk >= 0 and string[walk] == string[mid]:
        count += 1
        walk -= 1

    walk = mid + 1
    while walk < len(string) and string[walk] == string[mid]:
        count += 1
        walk += 1
    print(count)

