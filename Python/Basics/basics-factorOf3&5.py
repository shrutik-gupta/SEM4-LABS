"""For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are
multiples of three and five, print "FizzBuzz".
"""

for i in range(1,50):
    if (i%3==0 and i%5==0):
        print(i, "FizzBuzz")
    elif i%3==0:
        print(i, "Fizz")
    elif i%5==0:
        print(i, "Buzz")