def sumdivisors(n):
    counter = 1
    sum = 0
    while counter<=n:
        if n%counter==0:
            sum += counter
        counter += 1
    return sum