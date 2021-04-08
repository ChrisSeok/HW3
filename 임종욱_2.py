# C111152 임종욱

from random import randint

a = randint(0,100)
b = randint(0,100)
c = a + b

print(a,' + ', b,'의 값은? ',end=" ")
d = int(input())

if c == d:
    print('맞았습니다.')
else :
    print('틀렸습니다')
