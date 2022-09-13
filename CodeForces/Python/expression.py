a = int(input())
b = int(input())
c = int(input())

answers = [a+b*c, a*(b+c), a*b*c, (a+b)*c, a+b+c]
print(max(answers))