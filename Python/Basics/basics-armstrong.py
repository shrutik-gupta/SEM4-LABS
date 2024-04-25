num = int(input("Enter a number: "))
temp=num
result=0
while num!=0:
    rem = num%10
    result = result+rem**3
    num = num // 10

if temp==result:
    print("Armstrong")
else:
    print("Not an armstrong")
