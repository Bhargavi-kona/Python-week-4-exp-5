n=int(input("enter any number: "))
temp=n
reverse=0
while n>0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
if temp==reverse:
    print("palindrome: ",reverse)
else:
    print("not palindrome")
