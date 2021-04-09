#5번_B735042_김대겸

#복권번호 생성
import random
lotteryNumber = str(random.randint(10, 99))
#사용자 복권번호 입력
user_num = input("복권 번호(10~99사이)를 입력하시오: ")
#당첨발표
if (user_num[0] == lotteryNumber[0]) or (user_num[1] == lotteryNumber[1]):
    if (user_num[0] == lotteryNumber[0]) and (user_num[1] == lotteryNumber[1]):
        print("1등상 100만원에 당첨되셨습니다.")
    else:
        print("2등상 50만원에 당첨되셨습니다.")
else:
    print("상금은 없습니다.")