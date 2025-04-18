x=int(input("enter a number"))
for i in range(2,x):
    if x%i==0:
        print(x,"is not a prine number")
        break
else:
    print(x,"is a prime number")
