import copy
import importlib

modname = "problem8"
funcname = "find_largest_distance"
information = [[['test-cities-0.txt'], 3029], [['test-cities-1.txt'], 2613], [['test-cities-2.txt'], 2773], [['test-cities-3.txt'], 3741], [['test-cities-4.txt'], 2227], [['test-cities-5.txt'], 3145], [['test-cities-6.txt'], 2732], [['test-cities-7.txt'], 2573], [['test-cities-8.txt'], 2891], [['test-cities-9.txt'], 3465]]

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
