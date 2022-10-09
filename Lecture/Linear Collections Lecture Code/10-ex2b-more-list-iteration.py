#You are given two lists, x and y. Write code that prints out how many items in the two lists match (i.e., same value at same index)



def count_matches(x, y):
    count = 0
    size = len(x)
    if len(y) < len(x):
        size = len(y)

    for i in range(size):
        if x[i] == y[i]:
            count += 1

    return count


a = [0, 2, 4, 6, 10, 10]
b = [0, 3, 8, 6, 10, 11]



print("The number of matches was " + str(count_matches(a, b)))
