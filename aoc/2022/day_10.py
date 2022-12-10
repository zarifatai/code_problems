def signal_strength(i, x):
    i += 1
    if i == 20 or (i - 20) % 40 == 0:
        return i * x
    return 0


def pixel_value(i, x):
    if i >= x - 1 and i <= x + 1:
        return "#"
    return "."


x = 1
i = 0
j = 0
sum_strength = 0
pixel_vals = ""

for line in open("inputs/day10.txt"):
    line = line.strip()
    pixel_vals += pixel_value(j, x)
    i += 1
    j += 1
    j = j % 40
    sum_strength += signal_strength(i, x)
    if line == "noop":
        continue
    _, v = line.split()
    pixel_vals += pixel_value(j, x)
    i += 1
    j += 1
    j = j % 40
    x += int(v)
    sum_strength += signal_strength(i, x)

print(sum_strength)
display = [pixel_vals[i : i + 40] for i in range(0, len(pixel_vals), 40)]
for row in display:
    print(row)
