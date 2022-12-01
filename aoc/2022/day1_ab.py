from collections import Counter

with open("inputs/day1.txt") as f:
    lines = f.readlines()

maximum = 0
total_sum = 0
calories = {}
elf_idx = 0

for line in lines:
    line = line.replace("\n", "")
    if line == "":
        calories[elf_idx] = total_sum
        elf_idx += 1
        total_sum = 0
    else:
        total_sum += int(line)

counter = Counter(calories)
top_3 = counter.most_common(3)

print(sum([x[1] for x in top_3]))
