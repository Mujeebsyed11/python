#5.add odd and subtract even
n=int(input())
s1=str(n)
sodd=0
seven=0
for i in s1:
    if int(i)%2==0:
        seven+=int(i)
    else:
        sodd+=int(i)
print(sodd-seven)


