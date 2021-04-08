# C111152 임종욱

country = input('국가를 입력하시오: ')


# 국가가 한국의 경우 도를 물어본다.
if country == "한국" :
    state = input('도를 입력하시오: ')
    if state == "제주도" :
        cost = 10000
    else :
        cost = 5000
else :
    cost = 20000

print('배송료는 ',cost,'원입니다.')