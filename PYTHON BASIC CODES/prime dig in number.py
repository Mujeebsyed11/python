#6.prime dig in number
n=int(input())
l1=[1,2,3,5,7]
l2=[]
for i in str(n):
    if int(i) in l1:
        l2+=[int(i)]
print(l2)
