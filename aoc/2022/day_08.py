from operator import mul

forest = []
for line in open("inputs/day8.txt"):
    forest.append([int(x) for x in line.strip()])

perimeter = (2 * (len(forest[0]) + len(forest))) - 4

n_trees = 0
for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[0]) - 1):
        tree = forest[i][j]
        column = [row[j] for row in forest]
        left = max(forest[i][0:j])
        top = max(column[0:i])
        right = max(forest[i][j + 1 :])
        bottom = max(column[i + 1 :])
        if tree > left or tree > top or tree > right or tree > bottom:
            n_trees += 1
print(n_trees + perimeter)

max_mult = 0
for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree = forest[i][j]
        viewed_trees = []

        column = [row[j] for row in forest]
        left = forest[i][0:j][::-1]
        top = column[0:i][::-1]
        right = forest[i][j + 1 :]
        bottom = column[i + 1 :]

        for direction in (left, top, right, bottom):
            seen_trees = 0
            for x in direction:
                seen_trees += 1
                if x >= tree:
                    break
            viewed_trees.append(seen_trees)

        mult = 1
        for k in viewed_trees:
            mult = mul(k, mult)
        max_mult = max(max_mult, mult)
print(max_mult)
