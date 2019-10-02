from random import randint
a=randint(1,4)
s=int(input('введите число       '))
if a == s:
    print('pobeda')
elif a < s:
    print('меньше')
elif a>s:
    print('больше')
