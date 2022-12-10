with open("inputs/day2.txt") as f:
    read = f.read().splitlines()

inputs = [x.split(" ") for x in read]

# list in order of win, loss, draw
conditions = {
    "A": ["Y", "Z", "X"],
    "B": ["Z", "X", "Y"],
    "C": ["X", "Y", "Z"],
}

decisions_b = ["Z", "X", "Y"]

rewards = [6, 0, 3]

rewards_response = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

total_sum = 0
for action, response in inputs:
    response_idx = conditions[action].index(response)
    reward = rewards[response_idx] + rewards_response[response]
    total_sum += reward

total_sum_b = 0
for action, decision in inputs:
    reward_decision = rewards[decisions_b.index(decision)]
    response = conditions[action][decisions_b.index(decision)]
    reward_response = rewards_response[response]
    total_sum_b += reward_decision + reward_response

print(total_sum)
print(total_sum_b)
