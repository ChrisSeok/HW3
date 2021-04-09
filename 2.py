#2번_B735042_김대겸

#퀴즈생성
import random
x = random.randint(0, 100)
y = random.randint(0, 100)
print(x, "+", y, "의 값은?")
#정답 입력받기
user_ans = int(input("정답 :"))
#정답확인
if user_ans == (x + y):
    print("맞았습니다.")
else:
    print("틀렸습니다.")