length = 10
visited = [[0, 0]]
rope = [[0, 0] for _ in range(length)]


def update_tail(head, tail):
    x_delta = head[0] - tail[0]
    y_delta = head[1] - tail[1]
    if x_delta > 1 and y_delta > 1:
        return [head[0] - 1, head[1] - 1]
    if x_delta < -1 and y_delta < -1:
        return [head[0] + 1, head[1] + 1]
    if x_delta > 1 and y_delta < -1:
        return [head[0] - 1, head[1] + 1]
    if x_delta < -1 and y_delta > 1:
        return [head[0] + 1, head[1] - 1]
    if x_delta > 1:
        return [head[0] - 1, head[1]]
    if y_delta > 1:
        return [head[0], head[1] - 1]
    if x_delta < -1:
        return [head[0] + 1, head[1]]
    if y_delta < -1:
        return [head[0], head[1] + 1]
    return tail


for action in open("inputs/day9.txt"):
    direction, steps = action.strip().split()

    for _ in range(int(steps)):
        if direction == "R":
            rope[0][0] += 1
        if direction == "L":
            rope[0][0] -= 1
        if direction == "D":
            rope[0][1] -= 1
        if direction == "U":
            rope[0][1] += 1

        for i in range(len(rope) - 1):
            rope[i + 1] = update_tail(rope[i], rope[i + 1])
        visited.append(rope[-1])

covered = [(x, y) for x, y in visited]
print("Rope:", rope)
print("Positions covered:", len(set(covered)))
