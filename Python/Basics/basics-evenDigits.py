#find numbers between 100 and 400 (both included) where each digit of a number is an even number

for i in range(100,401):
    num=i
    digit1=num%10
    digit2=(num//10)%10
    digit3=num//100
    if(digit1%2==0 and digit2%2==0 and digit3%2==0):
        print(digit3,digit2,digit1,end=',')



    