import copy
import importlib
import random

modname = "problem6"
try:
    module = importlib.import_module(modname)
    process = getattr(module,"process")
    within_range = getattr(module,"within_range")
except Exception as e:
    print("Error loading module and/or function - check the names?")
    print("Error description: " + str(e))
    quit()

print("Case #1")
alist = [5, 1, 5, 0, 2, 1, 1, 4, 1, 3]
process(alist)
print("within_range(0,5) should be 10, your code produced: " + str(within_range(0,5)))
print("within_range(0,3) should be 7, your code produced: " + str(within_range(0,3)))
print("within_range(1,3) should be 6, your code produced: " + str(within_range(1,3)))
print("within_range(2,2) should be 1, your code produced: " + str(within_range(2,2)))
print("within_range(4,7) should be 3, your code produced: " + str(within_range(4,7)))

print("Case #2")
alist = [2, 4, 1, 3, 5, 3, 2, 1, 4, 3, 2, 4, 3, 5]
process(alist)
print("within_range(0,5) should be 14, your code produced: " + str(within_range(0,5)))
print("within_range(0,3) should be 9, your code produced: " + str(within_range(0,3)))
print("within_range(1,3) should be 9, your code produced: " + str(within_range(1,3)))
print("within_range(2,2) should be 3, your code produced: " + str(within_range(2,2)))
print("within_range(4,7) should be 5, your code produced: " + str(within_range(4,7)))

print("Case #3")
alist = [2, 7, 9, 4, 2, 4, 10, 5, 10, 5, 3, 8, 4, 6, 0, 3, 9, 3, 4, 0, 6, 5, 3, 1, 8, 2, 6, 7, 8, 2, 9, 0, 2, 9, 6, 4, 10, 6, 6, 8, 10, 9, 0, 2, 1, 9, 0, 7, 2, 1, 3, 9, 9, 5, 8, 7]
process(alist)
print("within_range(0,5) should be 29, your code produced: " + str(within_range(0,5)))
print("within_range(0,3) should be 20, your code produced: " + str(within_range(0,3)))
print("within_range(1,3) should be 15, your code produced: " + str(within_range(1,3)))
print("within_range(2,2) should be 7, your code produced: " + str(within_range(2,2)))
print("within_range(4,7) should be 19, your code produced: " + str(within_range(4,7)))


