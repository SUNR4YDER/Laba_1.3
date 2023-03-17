userstr = input()
userarr = list(userstr)
checker = 0
i = 0
while i<len(userarr):
    if(userarr[i].lower() == 'ф'):
        checker += 1
    i += 1
if (checker != 0):
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")
