from random import randint
a=randint(1,500)
for i in range(1,5) :
    l=(input('fghjkl   '))
    if l=='выход':
        break
    k=int(l)
    if k==a:
        print ('verno')
        break
    elif a<k :
        print('меньше',a)
    elif a>k :
        print('больше',a)


