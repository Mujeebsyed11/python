n=int(input())
s=str(n)
sum=0
for i in s:
    sum+=int(i)**len(s)
if sum==n:
    print(n,'is an armstrong number')
else:
    print(n,'is not an armstrong number')
