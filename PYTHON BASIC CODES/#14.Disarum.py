n=int(input())
s=str(n)
t=1
sum=0
for i in s:
    sum+=int(i)**t
    t+=1
if sum==n:
    print(n,'is a disarum')
else:
    print(n,'is not a disarum')
