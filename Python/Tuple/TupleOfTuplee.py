#check if a specified element appears in a tuple of tuples

ToT = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
colour = input("Enter colour you want to search for: ")
counter = 0
for tuple in ToT:
    if colour in tuple:
        counter+= 1
    
if(counter == 0):
    print("Colour not found")
else:
    print("Colour found")

