# C111152 임종욱

import random

lotteryNumber = random.randint(10, 99)

user_num = int(input('복권 번호(10~99사이)를 입력하시오: '))

if lotteryNumber == user_num :
    print('복권 번호는 ', lotteryNumber,'입니다. 1등상금은 100만원 입니다.')
elif ((lotteryNumber - user_num) % 10) or ((lotteryNumber - user_num) // 10) :
    print('복권 번호는 ', lotteryNumber,'입니다. 2등상금은 50만원 입니다.')
else :
    print('복권 번호는 ', lotteryNumber,'입니다. 상금은 없습니다.')
