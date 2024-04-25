num = int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of", num, "is", fact)

#recursive approach
a = int(input("Enter a number: "))
def factorial(a):
    if (a==1 or a==0):
        return 1
    else:
        return a*factorial(a-1)
    
print("Factorial of", a, "is", factorial(a))