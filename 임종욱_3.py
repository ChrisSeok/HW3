# C111152 임종욱

weight = float(input('무게(킬로그램): '))
height = float(input('키(미터): '))

bmi = weight/height**2

print('당신의 BMI: ', bmi)

if (bmi < 20) :
    print('저체중입니다')
elif (bmi >= 20) and (bmi <=24.9):
    print('정상입니다')
elif (bmi >= 25) and (bmi <=29.9):
    print('과체중입니다.')
elif (bmi >= 30) :
    print('비만입니다')
