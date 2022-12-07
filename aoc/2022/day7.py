from collections import defaultdict

sizes, in_scope = defaultdict(int), []

for line in open("day7.txt"):
    line = line.strip().split()
    if line[0] == "dir":
        continue
    elif line[0] == "$":
        if line[1] == "ls":
            continue
        elif line[1] == "cd":
            if line[2] == "..":
                in_scope.pop()
            elif in_scope:
                in_scope.append(in_scope[-1] + "/" + line[2])
            else:
                in_scope.append(line[2])
    else:
        for directory in in_scope:
            sizes[directory] += int(line[0])

values = sizes.values()
print("Total sum sizes below 100K:", sum([x for x in values if x <= 1e5]))

total_space, required_space = 7e7, 3e7
space_to_delete = required_space - (total_space - max(values))
print("Space to delete:", min([x for x in values if x >= space_to_delete]))
