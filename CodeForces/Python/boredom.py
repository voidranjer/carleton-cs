score = 0

input()
numbers = input().split()
numbers = [int(i) for i in numbers]

processed = []

for i in range(1, 11):
    processed.append(i * numbers.count(i))

while (sum(processed) > 0):
    # max_val = max(processed)
    # max_index = processed.index(max_val)

    i = 0
    while (processed[i] == 0):
        i += 1

    score += processed[i]
    processed[i] = 0

    if (i < len(processed)):
        processed[i + 1] = 0

    # processed[max_index] = 0
    # if (max_index != 0):
    #     processed[max_index - 1] = 0
    # if (max_index != len(processed) - 1):
    #     processed[max_index + 1] = 0

    # score += max_val

print(score)
