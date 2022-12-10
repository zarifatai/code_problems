with open("inputs/day6.txt") as f:
    input = f.read()

start_sequence_length = 14

curr_chars = ""
left = 0
right = start_sequence_length
while len(set(curr_chars)) < start_sequence_length:
    left += 1
    right += 1
    curr_chars = input[left:right]
print(right)
