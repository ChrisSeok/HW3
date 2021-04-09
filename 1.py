#1번_B735042_김대겸

nation = input("국가를 입력하시오: ")
if nation == "한국":
    do = input("도를 입력하시오: ")
    if do == "제주도":
        print("배송료는 10000원입니다.")
    else:
        print("배송료는 5000원입니다.")
else:
    print("배송료는 20000원입니다.")