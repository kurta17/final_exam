import math
number = input("enter your number: ")
def func(number):
    mylist = list(number)
    mylist.reverse()
    
    newlist = []
    for i in range(len(mylist)):
        x = int(mylist[i])
        if i % 2 == 0:
            x = x * 2
        newlist.append(x)
        
    print(newlist)
    new_list = []
    for m in newlist:
        
        m = int(m)
        if m > 10:
            m = m -9
        new_list.append(m)
    print(new_list)
    sum_digit = sum(new_list)
    checksum = (10 - sum_digit % 10) % 10
    return checksum





print(func(number))
