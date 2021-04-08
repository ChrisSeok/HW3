# 1번문제 / C111061 박서연 
nation = input('국가를 입력하시오: ')

if nation=='한국':
    district = input('도를 입력하시오: ')
    if district=='제주도':
        print('배송료는 10000원입니다.')
    else:
        print('배송료는 5000원입니다.')

else:
    print('배송료는 20000원입니다.')

