loc = int(input("Enter location after which you want to reverse the list: "))

ogList= [1,2,3,4,5,6,7,8,9]

revList= list(ogList[loc:])
revList.reverse()

nonRevList = list(ogList[:loc])

newList = nonRevList+revList
print(newList)