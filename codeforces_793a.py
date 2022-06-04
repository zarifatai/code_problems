t = int(input("Number of tests?\n"))

for _ in range(t):
    count = 1
    n_char = int(input("Number of characters in string?\n"))
    string = input("String?\n")

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

