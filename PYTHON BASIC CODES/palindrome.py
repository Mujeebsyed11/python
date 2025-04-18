#9.palindrome
n=int(input())
s=str(n)
if s[::-1]==s:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')
