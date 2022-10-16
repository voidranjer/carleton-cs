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

for i in range(xLength):  # list to search in
    x.append(random.randint(-10, 10))

for j in range(yLength):  # search list, aka numbers that will be searched for
    y.append(random.randint(-10000, 10000))

x.sort()  # sort the list

[binaryTimeTotal, pythonTimeTotal, binaryTimeAvg,
    pythonTimeAvg] = test(x, y, count)


print("Total time for binary search count : " + str(binaryTimeTotal))
print("Total time for python count(): " + str(pythonTimeTotal))
print("Average time for binary search count: " + str(binaryTimeAvg))
print("Average time for python count(): " + str(pythonTimeAvg))

# Analysis:
# 1. The binary search count is faster than the built-in count function
# 2. Doubling x causes a smaller increase in time taken for the binary search count function [O(log n)], but doubles the time taken for the linear built-in search function [O(n)]
# 3.
