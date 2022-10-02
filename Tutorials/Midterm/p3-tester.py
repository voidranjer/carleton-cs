
import copy
import importlib

modname = "part3"
funcname = "sumdivisors"
information = [[[62],96],
[[21],32],
[[21],32],
[[90],234],
[[21],32],
[[16],31],
[[77],96],
[[64],127],
[[13],14],
[[96],252],
[[36],91],
[[63],104],
[[70],144],
[[13],14],
[[25],31],
[[13],14],
[[81],121],
[[75],124],
[[63],104],
[[98],171],
[[23],24],
[[47],48],
[[17],18],
[[86],132],
[[99],156]]
resulttype = "int"

try:
    module = importlib.import_module(modname)
    func = getattr(module,funcname)
except Exception as e:
    print(e)
    print("Error loading module and/or function - check the names?")
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
