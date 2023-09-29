def func(mystr):
    mystr_len = len(mystr)
    if mystr_len % 2 == 0:
        mid_index = mystr_len // 2 - 1
        return mystr[mid_index:mid_index + 2]
    else:
        mid_index = mystr_len // 2
        return mystr[mid_index]



print(func("test"))
print(func("testing"))
print(func("middle"))