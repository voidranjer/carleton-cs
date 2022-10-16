import random
from binarytest import test


def count(list, value):
    end = findend(list, value)
    start = findstart(list, value)
    return end - start + 1


def findstart(list, value):  # find the point of first time value appears in a sorted list
    startIndex = 0
    endIndex = len(list) - 1
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2  # find the mid point index
        midValue = list[midIndex]  # find the mid point value
        if value == midValue:  # if the value == mid point value
            # check if either the values to the left are invalid (if mideindex -1 < 0) or if value and list[midindex -1] is not equal. This is for cases where the number is the first number or when the list goes over.
            if midIndex - 1 < 0 or value != list[midIndex-1]:
                return midIndex
            else:  # else treat it as if it is value < midpoint
                endIndex = midIndex - 1  # endValue becomes mid index - 1
        elif value > midValue:  # elif the value is > midpoint
            startIndex = midIndex + 1  # startValue becomes mid index + 1
        elif value < midValue:  # elif the value is < midpoint
            endIndex = midIndex - 1  # endValue becomes mid index - 1
    return 0


def findend(list, value):  # find the point of last time value appears in a sorted list
    startIndex = 0
    endIndex = len(list) - 1
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2
        midValue = list[midIndex]
        if value == midValue:
            if midIndex + 1 > len(list)-1 or value != list[midIndex+1]:
                return midIndex
            else:
                startIndex = midIndex + 1
        elif value > midValue:  # elif the value is > midpoint
            startIndex = midIndex + 1  # startValue becomes mid index + 1
        elif value < midValue:  # elif the value is < midpoint
            endIndex = midIndex - 1  # endValue becomes mid index - 1
    return -1


x = []
y = []
xLength = 2500
yLength = 50000
xDuplicates = 1

for i in range(xLength):  # list to search in
    for _ in range(xDuplicates):  # to test duplicate values in X
        num = random.randint(-10, 10)
        x.append(num)

for j in range(yLength):  # search list, aka numbers that will be searched for
    # to test case number 4 (larger proportions of Y not present in X, increase the range of randint in Y relative to X)
    y.append(random.randint(-10000, 10000))

x.sort()  # sort the list

[binaryTimeTotal, pythonTimeTotal, binaryTimeAvg,
    pythonTimeAvg] = test(x, y, count)


print("Total time for binary search count : " + str(binaryTimeTotal))
print("Total time for python count(): " + str(pythonTimeTotal))
print("Average time for binary search count: " + str(binaryTimeAvg))
print("Average time for python count(): " + str(pythonTimeAvg))

# Analysis:
# 1. The binary search count is faster than the built-in count function.
# 2. Doubling x causes a smaller increase in time taken for the binary search count function [O(log n)], compared to
#    the built-in count function which doubles the time taken [O(n)]
# 3. If X is changed to have more duplicate numbers, the relative efficiency of the binary search count function
#    will still be much higher than the built-in linear count function.
#    This is because of the binary count's O(log n) runtime complexity compared to the
#    built-in count's O(n) linear complexity.
#    Moreover, if we wanted to further optimize the entire sorting+searching process, we
#    could use the "Counting Sort" algorithm to deal with the duplicate values in the
#    sorting process.
#    However, without the "Counting Sort" algorithm, adding duplicate/non-duplicate
#    values to X will make minimal difference in time taken to count it provided
#    that the number of values added to X are equal (when adding either duplicate/non-duplicate values).
#    Additionally, even if the target number that is to be counted has a significant amount
#    of duplicate values in X, binary search count will still uphold its performance superiority
#    because it uses the binary search algorithm to determine the start and end of the target number streak in the sorted list.
# 4. If larger proportions of Y is not in X, when counting the numbers from Y that are not in X,
#    python's linear count() function's search space is still the entire list of X,
#    even if the number is not in X.
#    However, with binary search count, the search space/iteration count for numbers that are not in X
#    is only log2(n+1) and not the entire size of X itself.
# 5. The results make sense. With binary search, we sort X only once at the start of the
#    program, and perform additional count queries on the already sorted list, drastically
#    reducing the time complexity as the number of counts increases. With python's built-in
#    linear count() function, it does not perform any form of pre-processing (sorting the list in advance)
#    and has to search through every single element in X for each time it counts.
