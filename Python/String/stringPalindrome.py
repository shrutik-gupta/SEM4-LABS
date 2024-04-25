str = input("Enter a string: ")
str_rev = str[::-1]
if (str == str_rev):
    print("Palindrome")
else:
    print("Not a palindrome")

num_letters=0
num_digits=0
for char in str:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print(num_digits, num_letters)