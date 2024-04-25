row = int(input("Enter number of rows: "))

for i in range(row+1):
    for j in range(i):
        print("*", end='')
    print("\n")