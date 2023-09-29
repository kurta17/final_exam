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
    digit = sum_digit % 10
    checksum = 10 - digit
    if checksum == 10:
        print("0")
    else:
        print(checksum)





print(func(number))
