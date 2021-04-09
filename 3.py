#3번_B735042_김대겸

#BMI 측정
weight_kg = float(input("무게(킬로그램):"))
height_m = float(input("키(미터):"))
bmi = weight_kg / (height_m**2)
print("당신의 BMI:", bmi)
#비만도 판정
if 20 <= bmi <= 24.9:
    print("정상입니다.")
elif 25 <= bmi <= 29.9:
    print("과체중입니다.")
elif bmi >= 30:
    print("비만입니다.")
