import copy
import importlib

modname = "problem5"
funcname = "box_weight"
information = [[[[2, 1, 4, 2, 9, 7, 2, 1, 3, 1, 2, 3, 9, 4]], 50], [[[2, 1, [[4], 2, [9, 7]], 2, [1, 3, [1, [2], [3]], [9], [], 4]]], 50], [[[10, 10, 7, 5, 10, 6, [2, 1, 6], 7, 3]], 67], [[[[4, 10, 9], [2, [9, [4, [5, 4, 10, 3], [5, 8, 5, 2]]], [[3, 6], [7, [2, 10]]], 4], 7, 8, [9, 7], 3, 6, [2, [[3, 5], 9, 8], 3], 10]], 192], [[[[[[1, [10, 8, [3, 8]]], 9], 1, 4, 9], 7, 1, 8, 9, 4, [[8, 4, 8], 7, 5], 9, 4, 3]], 130], [[[3, 8, 7, [1, 9, 3, 10], [[[2, 3], 7, [10, 1]], 8], [5, 8, [4, 7]], 8, 9, 6, 3, 1]], 123], [[[8, 10, 2, 3, 10, 3, 10, 5]], 51], [[[9, [5, [5, 9, [10, 10, 9, 8], [[3, 8, [7, 1], 9], 2, 3, 2]]], 9, 9, 7, [10, [3, 9], [10, [4, [2, 10, 7]]]], [8, 5], [[8, 4, 6, 5], 3], 10, [8, 1], [[[2, 5, 3, 3], 5, [2, 8, 3, 1], 10], 10]]], 290], [[[5, 4, [9, 8, [[[9, 10, 6, 9], [[4, 2, 8], 3], 6], 2, [7, 4, 4, 3], 8]], [4, 7], 8, [5, [9, 7], 10], 5, 2, [6, 1], 10, [[8, 2, [[5, 1, 2], [10, [5, [8, 3]], [4, 3, [9, 1]]], 4], 6], 8, 9], 5, 3, [[4, 10, 4, 2], 2, 10, 5], 6]], 324], [[[3, 7, 9, [[[6, 1, 1], 4, [[[6, 8], 4], [1, [6, 8, [5, 9, 10, [6, 1, 7]], [[3, 7, [10, 8, 7], 4], 7, 4]], 1, [[1, [[9, [6, 9, 1, 9]], 2, [[8, 3, [6, 9, 1]], 1, 2, 5]], 7], [8, 7], 3]], 10, 8], 6], 8], [[4, [3, 9, 8], 1], 10], 6, 6, 9, 8, 7]], 353], [[[6, 9, 3, [[3, 4, [2, 8, 2, 8], 4], [4, 9, 6, 10]], [4, 2], 3, 4, 10, 10, [[[8, 1, 3], [2, 7, 3, 6]], 10, 5]]], 156], [[[8, 5, 4, 8, 4, 10, 7, 10, 5, 5, [7, 10, 8], 1]], 92], [[[1, 9, 9, [[[4, 8, 2], [1, 1, 8, 10], 5, [[9, 5], 1]], 2, 6, 5], [[[[[7, 1, 3], [[5, 4], [3, [9, [4, [7, 9, 5]]]], 6], 6], 3, 2, [2, [2, 1, [7, 2, 1, 6]]]], 5], 9, [[8, 3], 10, [4, 4, 10]], 3], 3, [7, 2, 8], [8, 7, 5], [7, 7, 3, 7], 3, 10, 10]], 324], [[[2, 3, [[3, 8], [8, [[[3, [3, [7, 1, 8]], 10, 8], [6, 3, 5], 8], [3, 1, [[4, 1, [6, 9, 1], 7], 9, 5, 8]], 7]], 8], [[[[4, 4], 7, [6, [6, 1]]], 6], 8, [6, 10, [10, [4, 4, 3], 8]], 1], [10, 2, 6], 4, 7, 3, 1, 8]], 284], [[[5, 8, 8, [[3, 5, [6, [9, [2, 6, 3]], 6, 5]], 3, 8], [[9, [4, 3], 7, 2], 7, 7, 9], 9, [4, [9, [[10, 9], 6], 7]], 3, 5]], 187], [[[[[2, [10, 6, [[2, 2, [1, [5, 10, 8]], 1], [[6, 2, [5, 10, [9, [6, 8, 10]], 2], 3], 3], [[1, [2, [3, 3], [4, 4]], 10, 8], 4, 6], 5]], 1, [7, [10, 1]]], 9, 8], 9, [[[2, 6], 7], 5], [[1, 7, [[[7, 6, 7, 4], 7], 3], 10], 2], 6, 8, 5, 9]], 308], [[[[1, 3], 10, 1, [[9, [9, 1, 6]], [6, [1, 8, 8, 6], 2, 7], [[9, 9], 9, [7, 2, 10], 7]], [2, [9, 10]], [[1, [9, [5, 4, 2], 8], [10, 3]], 3, 9], 7, 1, 5, 10, [6, 10, [[3, [5, 1], 10], 6, [[10, 4], [[10, 1], [10, 1, 1, 10], 10, 1], [[5, 6], 7, [[8, [[[6, [3, 3, [[5, 10], 9, [[6, 7, [[10, 3], 8, 2, [1, 9, [2, 8, 8]]]], 1, 6, 9], [3, [7, 6, 2], 4]], [3, 3, [6, 6], 1]], 6], 8, 4, 8], [[3, 4, 5], 1], [[[3, 9, 6, [7, 8, 10, 5]], [3, 8, 3, [[[[2, [6, [7, 7, 2, 8], 1], 6, 4], 9, 5, 8], 1, 9, 7], 7]], 5, 10], 2]], 8], [1, 10, 2]]], 8], 9], 6]]], 762], [[[[8, 5, [6, 3, 10]], [7, 10, 7, [[[6, 6, 3, 5], 10], 3, 3]], 7, 5, 7, 8]], 119], [[[[7, 5, 1, 6], 7, 7, 10, [3, 7, [7, [[[3, [[4, 3], [2, [2, 10], 5, 1], [[3, [2, 4], 2, 6], 6, 9, [4, [7, 10, [7, [2, 2, 3, [8, 4, 6, [6, 8, 4]]], [8, [3, 3, 9], 3, 4]], 3]]]], 9], 1], 4, [9, 7], [2, 4]], 8, 8]], 9, 4, 5, 5]], 301], [[[[7, 4], [9, 3, 4, 1], 2, [4, 10, 6, [8, 6]], 4]], 68], [[[4, 7, [2, 6], 7, 8, 3, [[[[6, [3, 2, 7, [10, 6, 10, 7]]], 9], 10], 5], [[[1, [6, 3]], 7, [7, 10, [7, 2]], [[[2, 1, 4], 9, [8, 5, 1, [6, [[[7, 2, [4, 9, 7, [10, 8, [1, 5, 10], 3]], [3, [1, 6, 10]]], 5, 7], [4, 5], [6, [8, 6], 5, 5], [5, 1, 6]], 2, 6]]], [1, 3, [7, 10, [1, 7, 6, [10, 1, 9]], [6, [3, 6], 2, [8, 5, 6]]]]]], 6, [2, 8, 10], 8], [8, 8]]], 489], [[[2, 3, 7, 2, [2, 8, 3], 5, 8, 4]], 44], [[[[4, 5, 1], 5, [8, [9, 6, 7, 4], 2, [7, 5, 7]], 4, [9, 10, [8, [[[2, [[9, [5, 9, 4, [10, [3, [[8, 5], [5, 9], [4, 9, [4, [8, 7], 2]]], [7, [[5, 1, [[[[6, [6, [5, 7, [2, [3, 8, 2, [[8, 8, [6, 2, 8, 9]], 9, 4]]]], 4], 4], 8, 4, [1, [2, 5, 10], [9, 10]]], [3, 1, 9], 8, 2], 2, 9], 1], 6, [[9, 6, 5, 4], 7, 3], 3]]], 2, 5]], 8], [[5, 2, 8, 5], 8]], 3, [3, [1, 2], [2, 1], 9]], [5, 3]], [2, [1, 3, 3], 3, 6]], 3], 9], [1, 6], 4, 2, [[[3, [9, 3, 3], 10, 5], 5, 9], [7, [10, 10]]], 9]], 643], [[[5, 7, 6, 1, 4, 4, 7, 5, 4, 4]], 47], [[[2, 4, 9, 10, 4, 4, 10]], 43]]
resulttype = "int"

try:
    module = importlib.import_module(modname)
    func = getattr(module,funcname)
except Exception as e:
    print("Error loading module and/or function - check the names?")
    print("Error description: " + str(e))
    quit()

correct = 0
incorrect = []
print("Checking function with test inputs...")
print()
for info in information:
    inputs = copy.deepcopy(info[0])
    goal = info[1]
    print("Inputs:", str(inputs)[1:-1])
    print("Goal:",goal)
    result = func(*inputs)
    print("Your Result:", result)
    success = False
    if resulttype == "int" and isinstance(result, int):
        success = goal == result
    elif resulttype == "float" and isinstance(result, (int,float)):
        success = abs(goal - result) < 0.001
    elif resulttype == "string" and isinstance(result, str):
        success = goal.lower() == result.lower()
    elif resulttype == "orderedlist" and isinstance(result, list):
        success = False
        if len(goal) == len(result):
            success = True
            for i in range(len(goal)):
                if goal[i] != result[i]:
                    success = False

    if success:
        correct += 1
        print("Good!")
    else:
        incorrect.append([inputs,goal,result])
        print("Incorrect!")
    print()

print()
print("Your code produced",correct,"out of", len(information),"correct results.")
print()

if len(incorrect) > 0:
    input("Hit enter to see the incorrect cases...")
    print("The inputs for which your program failed were:")
    print()
    for info in incorrect:
        print("Inputs:", str(info[0])[1:-1])
        print("Goal:", info[1])
        print("Your Result:", info[2])
        print()
