#4번_B735042_김대겸

user_int = int(input("정수를 입력하시오: "))
if (user_int % 2 == 0) or (user_int % 3 == 0):
    if (user_int % 2 == 0) and (user_int % 3 == 0):
        print("2와 3으로 동시에 나누어지는 수.")
    else:
        print("2또는 3으로 나누어지지만 2와 3으로 동시에 나누어지지는 않는 수.")
else:
    print("2또는 3으로 나누어지지 않는 수.")
