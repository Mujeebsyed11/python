#2.prime number checking
n=int(input())
sum=0
for i in range(2,n):
    if n%i==0:
        print(n,'is not a prime')
        break
else:
    print(n,'is a prime')
