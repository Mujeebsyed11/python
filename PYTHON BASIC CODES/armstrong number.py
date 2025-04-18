import math
n=int(input())
str1=str(n)
sum=0
for i in str1:
    sum=sum+(int(i)**len(str1))
if sum == n:
    print('armstrong number')
else:
    print('not armstrong number')
