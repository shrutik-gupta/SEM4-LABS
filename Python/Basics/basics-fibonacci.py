# get the Fibonacci series between 0 and 50.
a = 0
b=1
fiboList = []
while a<=50:
    fiboList.append(a)
    a=b
    b=a+b
print(fiboList)

# get the Fibonacci series till a given index
num1 = 0
num2=1
desired = int(input("Enter last index you want fibonacci series of: "))
fiboList1 = []
while (len(fiboList1)<=desired):
    fiboList1.append(num1)
    num1=num2
    num2=num1+num2
print(fiboList1)