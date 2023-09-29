mystr = input("enter your string: ")


def func(mystr):
    mydict = {}
    answer = 0
    for i in mystr:
        if i.isalnum():
            char_lower = i.lower()
            mydict[char_lower] = mydict.get(char_lower, 0) + 1
            if mydict[char_lower] == 2:
                answer += 1

    return answer


print(func(mystr))

