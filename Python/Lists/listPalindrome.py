lst = [1,2,2,2,1]
def palindrome(lst):
    revLst = lst[::-1]
    if revLst==lst:
        return True
    else:
        return False
    
print(palindrome(lst))

lst2=[4,5,6,78,1,2]

unionList = list(set(lst+lst2))
intersectionList = list(set(lst-lst2))

print(unionList, intersectionList)