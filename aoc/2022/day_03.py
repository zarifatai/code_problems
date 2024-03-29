with open("inputs/day3.txt") as f:
    inputs = f.read().splitlines()


def get_priority(unicode):
    if unicode <= 90:
        return unicode - 38
    return unicode - 96


# part a
result_a = 0
for i in inputs:
    first_compartment = i[: int(len(i) / 2)]
    second_compartment = i[int(len(i) / 2) :]
    both_compartments = list(set(first_compartment).intersection(second_compartment))
    unicode = ord(both_compartments[0])
    result_a += get_priority(unicode)

# part b
result_b = 0
for i in range(2, len(inputs), 3):
    elf_1, elf_2, elf_3 = inputs[i - 2 : i + 1]
    all_elves = list(set(elf_1).intersection(elf_2).intersection(elf_3))
    unicode = ord(all_elves[0])
    result_b += get_priority(unicode)

print(result_a, result_b)
