input()
numbers = input().split()
numbers = [int(i) for i in numbers]
for i, n in enumerate(numbers):
    print(numbers.index(i + 1) + 1)