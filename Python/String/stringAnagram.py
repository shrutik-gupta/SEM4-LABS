str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
str1_sorted = sorted(str1) #converts to list and sort in ascending
str2_sorted = sorted(str2)

if str1_sorted==str2_sorted:
        print("Anagram")
else:
        print("Not anagram")