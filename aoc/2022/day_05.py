import copy

with open("inputs/day5.txt") as f:
    input = f.read()

crates_input, instructions_input = input.split("\n\n")
crates_input = crates_input.splitlines()
n_of_stacks = int(crates_input[-1].strip()[-1])

crates = crates_input[:-1][::-1]
stacks_a = [[] for _ in range(n_of_stacks)]

for level in crates:
    right = 4
    stack_idx = 0
    for left in range(0, len(level), 4):
        crate = level[left:right].strip(" []")
        if crate != "":
            stacks_a[stack_idx].append(crate)
        right = right + 4
        stack_idx += 1

stacks_b = copy.deepcopy(stacks_a)

instructions_input = instructions_input.splitlines()

for idx, instruction_input in enumerate(instructions_input):
    instruction = instruction_input.split(" ")
    move = int(instruction[1])
    frm = int(instruction[3]) - 1
    to = int(instruction[5]) - 1
    multi_crates = []
    for _ in range(move):
        crate = stacks_a[frm].pop()
        stacks_a[to].append(crate)
        multi_crate = stacks_b[frm].pop()
        multi_crates.append(multi_crate)
    for x in multi_crates[::-1]:
        stacks_b[to].append(x)

result_a = ""
result_b = ""
for i in range(n_of_stacks):
    if stacks_a[i]:
        result_a += stacks_a[i].pop()
    if stacks_b[i]:
        result_b += stacks_b[i].pop()

print(result_a, result_b)
