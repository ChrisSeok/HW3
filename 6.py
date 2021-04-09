6번 C135192 송이현
>>> x=int(input("첫 번째 정수: "))
첫 번째 정수: 34
>>> y=int(input("두 번째 정수: "))
두 번째 정수: 52
>>> z=int(input("세 번째 정수: "))
세 번째 정수: 10
>>> if x<y<z
 print("중간값은 y이다.")
 else y<x<z
 print("중간값은 x이다.")
 else y<z<x
 print("중간값은 z이다.")
 else z<x<y
 print("중간값은 x이다.")
 else z<y<x
 print("중간값은 y이다.")
 else x<z<y
 print("중간값은 z이다.")