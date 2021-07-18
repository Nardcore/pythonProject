text = input().split(' ')
alfeng = 'abcdefghijklmnopqrstuvwxyz'
alfengup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(text)
def kolvo_bukv(slovo): # посчитаем сдвиг
    count = 0
    for i in slovo:
        if i.isalpha():
            count += 1
    return int(count)
def shifr_cesar(text): # функция шифрования
    shifr = ''
    for i in text:
        for j in i:
            if j.isalpha():
                if j in alfengup:
                    if (int(alfengup.index(j)) + kolvo_bukv(i)) >= len(alfengup):
                        shifr += alfengup[int (alfengup.index (j)) + kolvo_bukv(i) - len(alfengup)]
                    else:
                        shifr += alfengup[int(alfengup.index(j)) + kolvo_bukv(i)]
                elif j in alfeng:
                    if (int (alfeng.index (j)) + kolvo_bukv(i)) >= len(alfeng):
                        shifr += alfeng[int (alfeng.index (j)) - len (alfeng) + kolvo_bukv(i)]
                    else:
                        shifr += alfeng[int (alfeng.index (j)) + kolvo_bukv(i)]
            else:
                shifr += j
        shifr += ' '
    return shifr
print(shifr_cesar(text))