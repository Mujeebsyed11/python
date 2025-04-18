#3.To print prime numbers in a given range
x=int(input())
y=int(input())
for i in range(x,y+1):
    sum=0
    for j in range(2,i):
        if i%j==0:
            sum+=1
    if sum==0:
        print(i,' is a prime number')
