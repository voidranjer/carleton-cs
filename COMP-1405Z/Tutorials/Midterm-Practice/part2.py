def gcf(x, y):
    gcd = 1
    counter = 1
    min = x

    if x<1 or y<1:
        return -1

    if x>y:
        min = y

    while counter<=min:
        if x%counter==0 and y%counter==0:
            gcd = counter
        counter += 1
    return gcd

print(gcf(int(input("First number: ")),int(input("Second number: "))))