with open("inputs/day1.txt") as f:
    input = f.read().strip().split("\n\n")

cals = sorted([sum(map(int, elf.split("\n"))) for elf in input])

print(cals[-1])
print(sum(cals[-3:]))
