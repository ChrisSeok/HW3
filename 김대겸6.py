#6번_B735042_김대겸

#숫자 입력받기
num_1 = int(input("숫자 1:"))
num_2 = int(input("숫자 2:"))
num_3 = int(input("숫자 3:"))
medium_num = 0
#중간 숫자 출력
if (num_1 > num_2):
    if (num_2 > num_3):
        medium_num = num_2
    else:
        if (num_1 > num_3):
            medium_num = num_3
        else:
            medium_num = num_1
else:
    if (num_2 < num_3):
        medium_num = num_2
    else:
        if (num_1 > num_3):
            medium_num = num_1
        else:
            medium_num = num_3
print("중간값은 :",medium_num)
