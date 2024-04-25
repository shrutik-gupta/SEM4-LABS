def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Unsopported operand type")
    else:
        print("Result of division is:", result)
    finally:
        print("Division performed")

divide(10,0)
divide('10',0)
divide(10,2)