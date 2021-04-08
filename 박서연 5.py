#5번문제 
import random
lotteryNumber = random.randint(10, 99)

myNum = int(input('복권 번호(10-99사이)를 입력하시오: '))

if myNum==lotteryNumber:
             print('복권번호는', lotteryNumber, '입니다. 상금은 100만원 입니다.')

elif myNum/10==lotteryNumber/10 or myNum%10==lotteryNumber%10:
            print('복권번호는', lotteryNumber, '입니다. 상금은 50만원 입니다.')

else:
    print('복권번호는', lotteryNumber, '입니다. 상금은 없습니다.')