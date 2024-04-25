#Multiplication table (from 1 to 10) of a number

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"X", i,'=', num*i)