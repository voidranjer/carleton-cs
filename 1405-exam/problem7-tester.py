import copy
import importlib

modname = "problem7"
funcname = "coldest_interval"
information = [[[[-9, -2, -3, 4, 8, -3, -2, -10, -2, -7], 1], -10], [[[-9, -2, -3, 4, 8, -3, -2, -10, -2, -7], 10], -2.6], [[[-9, -2, -3, 4, 8, -3, -2, -10, -2, -7], 3], -6.333333333], [[[7, 6, -2, -6, -2, 0, -5, 10, -3, 10], 1], -6.0], [[[7, 6, -2, -6, -2, 0, -5, 10, -3, 10], 3], -3.3333333333333335], [[[7, 6, -2, -6, -2, 0, -5, 10, -3, 10], 10], 1.5], [[[-4, 5, 3, 6, -4, -9, 9, 3, -4, -6, -4, 1, 6, -9, -6, -4, 7, -6, 7, 6, -8, 4, -2, 0, 9, -5, 0, -8, -7, -2], 3], -6.333333333333333], [[[-4, 5, 3, 6, -4, -9, 9, 3, -4, -6, -4, 1, 6, -9, -6, -4, 7, -6, 7, 6, -8, 4, -2, 0, 9, -5, 0, -8, -7, -2], 5], -4.4], [[[-4, 5, 3, 6, -4, -9, 9, 3, -4, -6, -4, 1, 6, -9, -6, -4, 7, -6, 7, 6, -8, 4, -2, 0, 9, -5, 0, -8, -7, -2], 10], -2.5], [[[2, -9, -2, 6, 2, 10, 5, -8, 0, 2, -4, 9, 8, -7, -7, 6, 8, 6, -5, 4, -9, -9, -6, 1, 1, -1, 9, 4, -7, 4], 3], -8.0], [[[2, -9, -2, 6, 2, 10, 5, -8, 0, 2, -4, 9, 8, -7, -7, 6, 8, 6, -5, 4, -9, -9, -6, 1, 1, -1, 9, 4, -7, 4], 5], -5.0], [[[2, -9, -2, 6, 2, 10, 5, -8, 0, 2, -4, 9, 8, -7, -7, 6, 8, 6, -5, 4, -9, -9, -6, 1, 1, -1, 9, 4, -7, 4], 10], -1.9], [[[-10, -9, -1, -10, 9, 0, -2, -4, 0, -1, -7, -7, -1, -5, 2, -10, 9, 5, 3, -3, -4, -6, 8, -4, -4, -4, 0, 4, 6, -5, -3, 10, -4, 5, -5, 3, 9, -7, 2, -2, 0, 5, 7, -6, -7, -2, 6, 0, -9, -10, -7, 6, -1, 4, 1, -8, 7, 9, 7, -8, 1, -3, 5, -6, 3, 10, 9, -7, 0, 1, 3, -9, -3, -10, -4, -2, -1, 1, 4, 4, 3, 6, 10, -6, -7, -8, -7, -9, -7, -5, -4, -6, -9, -6, -9, -4, 4, 3, -5, 2], 3], -8.666666666666666], [[[-10, -9, -1, -10, 9, 0, -2, -4, 0, -1, -7, -7, -1, -5, 2, -10, 9, 5, 3, -3, -4, -6, 8, -4, -4, -4, 0, 4, 6, -5, -3, 10, -4, 5, -5, 3, 9, -7, 2, -2, 0, 5, 7, -6, -7, -2, 6, 0, -9, -10, -7, 6, -1, 4, 1, -8, 7, 9, 7, -8, 1, -3, 5, -6, 3, 10, 9, -7, 0, 1, 3, -9, -3, -10, -4, -2, -1, 1, 4, 4, 3, 6, 10, -6, -7, -8, -7, -9, -7, -5, -4, -6, -9, -6, -9, -4, 4, 3, -5, 2], 5], -7.6], [[[-10, -9, -1, -10, 9, 0, -2, -4, 0, -1, -7, -7, -1, -5, 2, -10, 9, 5, 3, -3, -4, -6, 8, -4, -4, -4, 0, 4, 6, -5, -3, 10, -4, 5, -5, 3, 9, -7, 2, -2, 0, 5, 7, -6, -7, -2, 6, 0, -9, -10, -7, 6, -1, 4, 1, -8, 7, 9, 7, -8, 1, -3, 5, -6, 3, 10, 9, -7, 0, 1, 3, -9, -3, -10, -4, -2, -1, 1, 4, 4, 3, 6, 10, -6, -7, -8, -7, -9, -7, -5, -4, -6, -9, -6, -9, -4, 4, 3, -5, 2], 10], -7.0]]
resulttype = "float"

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
