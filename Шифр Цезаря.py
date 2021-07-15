text = 'To be, or not to be, that is the question!'
s = 17
alf = 'abcdefghijklmnopqrstuvwxyz'
alfup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shifr = ''
for i in text:
    if i.isalpha() and i in alf:
        if int(alf.index(i)) + s > len(alf):
            shifr += alf[(int (alf.index (i)) - len(alf)) + s]
        else:
            shifr += alf[int (alf.index (i)) + s]
    elif i.isalpha() and i in alfup:
        if int (alfup.index(i)) + s > len(alfup):
            shifr += alfup[(int (alfup.index (i)) - len(alfup)) + s]
        else:
            shifr += alfup[int (alfup.index (i)) + s]
    else:
        shifr += i
print (shifr, end='')
