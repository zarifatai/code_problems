with open("inputs/day4.txt") as f:
    pairs = f.read().splitlines()

count_a = 0
count_b = 0
for pair in pairs:
    e1, e2 = [x.split("-") for x in pair.split(",")]
    e1_start, e1_end = [int(x) for x in e1]
    e2_start, e2_end = [int(x) for x in e2]

    if (e1_start <= e2_start and e1_end >= e2_end) or (
        e2_start <= e1_start and e2_end >= e1_end
    ):
        count_a += 1

    if (e1_end >= e2_start and e2_start >= e1_start) or (
        e1_start <= e2_end and e1_end >= e2_start
    ):
        count_b += 1

print(count_a)
print(count_b)
