n=int(input())
s=str(n)
t=s[::-1]
sum=0
if s==t:
    for i in range(2,n):
        if n%i==0:
            sum+=1
else:
    print(n,'is not a palyprime')
if sum==0:
    print(n,'is a palyprime')
else:
    print(n,'is not a palyprime')
