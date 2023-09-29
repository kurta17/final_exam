
def func(mylist):
    if not mylist:
        return 0
    else:
        return mylist[-1] + func(mylist[:-1])



print(func([1,1,2,5,5,5]))


