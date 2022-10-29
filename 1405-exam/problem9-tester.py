import copy
import importlib

modname = "problem9"
funcname = "sort_volumes"
information = [[['test-volumes-0.txt'], [932062, 473406, 746794, 129734, 736504, 212889, 698922, 989000, 854355, 885101]], [['test-volumes-1.txt'], [678030, 854973, 535977, 921717, 555880, 490403, 170955, 205841, 155269]], [['test-volumes-2.txt'], [254395, 771011, 178412, 750241, 781831, 699569, 325352, 442979, 844699, 888021, 590450, 433455, 986850, 724397, 801016, 427451, 429224, 875906, 823730, 975723, 601347, 311228]], [['test-volumes-3.txt'], [713848, 193894, 419291, 804836, 594743, 799079, 190701, 865652]], [['test-volumes-4.txt'], [267728, 824262, 434112, 917778, 652637, 730371, 976731, 958414, 703753, 790895, 444044, 104299, 712210, 443432, 253311, 564953, 311187, 991904, 365442, 907439, 475949, 629501, 696769, 154660, 386358]], [['test-volumes-5.txt'], [248117, 840619, 644563, 692149, 177497, 335850, 817074]], [['test-volumes-6.txt'], [616072, 810323, 672848]], [['test-volumes-7.txt'], [729053, 244601, 228609, 281179, 455466, 495138, 926176, 460231, 679482, 513703, 496161, 756398, 596309, 265844, 143277, 287066, 304098]], [['test-volumes-8.txt'], [253509, 514125, 593098]], [['test-volumes-9.txt'], [905457, 585504, 987965, 212074]]]

resulttype = "orderedlist"

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
