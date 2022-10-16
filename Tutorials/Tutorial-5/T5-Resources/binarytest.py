import time


def test(x, y, count):
    binaryTimeTotal = 0
    pythonTimeTotal = 0

    for item in y:
        startTime = time.time()
        funcCount = count(x, item)
        binaryTimeTotal += (time.time() - startTime)

        startTime = time.time()
        pyCount = x.count(item)
        pythonTimeTotal += (time.time() - startTime)

        if pyCount != funcCount:
            print(funcCount)
            print(pyCount)
            break

    length = len(y)
    binaryTimeAvg = binaryTimeTotal / length
    pythonTimeAvg = pythonTimeTotal / length

    return [binaryTimeTotal, pythonTimeTotal, binaryTimeAvg, pythonTimeAvg]
