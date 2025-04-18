#1.To print factors of a number
n=int(input())
list1=[]
for i in range(1,n+1):
    if n%i==0:
        list1=list1+[i]
print(list1)
        
