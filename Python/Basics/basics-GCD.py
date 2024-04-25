def gcd(a, b):
    while (b!=0):
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
