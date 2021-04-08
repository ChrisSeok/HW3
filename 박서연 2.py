#2번문제 
import random

x = random.randint(0, 100)
y = random.randint(0, 100)

print(x, '+', y, '의 값은?', end='')
sum = int(input())

if sum==x+y:
    print('맞았습니다.')
else:
    print('틀렸습니다.')