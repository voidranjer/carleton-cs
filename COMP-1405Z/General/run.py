# Emily Mei Lin Chan Cheung Shing
# 101276521

num_1 = int(input ("Enter an integer: "))
divisor = 0
sum = 0

print("The divisors are: ")
while divisor <= num_1 :
    divisor += 1
    if (num_1 % divisor == 0 ) :
        print(divisor)
        sum += divisor
print ("The sum of all the divisors is " + str(sum))
if num_1 == (num_1 + 1):
    print (num_1, "is a prime number")
else: print(num_1, "is not a prime number")

num_2 = int(input ("Enter an integer: "))
divisor = 0
sum=0
stop = num_2 + 1
for divisor in range(0,stop + 1,1) :
    divisor += 1
    if (num_2 % divisor == 0 ) :
        print(divisor)
        sum += divisor
print ("The sum of all the divisors is " + str(sum))
if num_2 == (num_2 + 1):
    print (num_2, "is a prime number")
else: print(num_2, "is not a prime number")