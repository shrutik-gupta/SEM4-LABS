# check if a triangle is equilateral, isosceles or scalene

side1 = float(input("Enter side 1 of triangle: "))
side2 = float(input("Enter side 2 of triangle: "))
side3 = float(input("Enter side 3 of triangle: "))

if (side1==side2==side3):
    print("Equilateral triangle")
elif (side1!=side2!=side3!=side1):
    print("Scalene triangle")
else:
    print("Isoscales triangle")