row = int(input("Enter number of rows: "))

for i in range(row+1):
    for j in range(i):
        print("*", end='')
    print("\n")
print("--------------------------")

for i in range(row+1):
    for k in range(row-i):
        print(" ",end="")
    for j in range(i):
        print("*", end='')
    print("\n")
print("--------------------------")

for i in range(row,0,-1):
    for j in range(i):
        print("*", end='')
    print("\n")