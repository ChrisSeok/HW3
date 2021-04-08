#4번문제 
number = int(input('정수를 입력하시오: '))

if number%2==0 and number%3==0:
    print('2와 3으로 동시에 나누어지는 수.')

elif number%2==0 or number%3==0:
    print('2또는 3으로 나누어지지만 2와 3으로 동시에 나누어지지 않는 수.')

else:
    print('2또는 3으로 나누어지는 수가 아님.')