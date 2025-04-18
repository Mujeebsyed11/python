#10.emirp number
n=int(input())
s=str(n)
m=int(s[::-1])
sum=0
for i in range(2,n):
    if n%i==0:
        break
else:
    for j in range(2,m):
        if m%j==0:
            sum+=1
            break
if sum==0:
    print(n,' is an emirp')
else:
    print(n,'is not an emirp')
