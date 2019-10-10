a=input()
b =input()
c=input()
try: int(a)
except ValueError:
    print('ошибка')
try: int(b)
except ValueError:
    print('ошибка')
if c == '+':
    print(int(a)+int(b))
elif c == '-':
    print(int(a)-int(b))
elif c == '*':
    print(int(a)*int(b))

elif c == '/':
     try: int(a)/int(b)
     except ZeroDivisionError:
        print('ошибка 0')
else: print(int(a)/int(b))
