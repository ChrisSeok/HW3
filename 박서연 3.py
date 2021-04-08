#3번문제 
weight = int(input('무게(킬로그램):'))
height = float(input('키(미터):'))

x = weight / height**2
print('당신의 BMI:', x)
bmi = x

if bmi>=30:
    print('비만입니다.')
if bmi>=25 and bmi<=29.9:
    print('과체중입니다.')
if bmi>=20 and bmi<=24.9:
    print('정상입니다.')
