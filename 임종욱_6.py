# C111152 임종욱

a = int(input('숫자 1: '))
b = int(input('숫자 2: '))
c = int(input('숫자 3: '))

#  입력받은 정수를 크기순으로 나열하기위해 리스트로 만든다
order = [a,b,c]

# 두 정수의 크기를 비교하여 왼쪽의 수가 클 경우 두 수의 위치를 바꾼다
# 과정이 끝나면 리스트안의 수가 크기별로 정렬된다.
if order[0] >order[1]:
  order[0],oder[1] = order[1],order[0]
if order[1] > order[2]:
  order[1],order[2] = order[2],order[1]

median = int(order[1])

print('중간값은 ', median)