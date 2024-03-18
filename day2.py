temp = int(input("온도를 입력하시오: "))

if temp >= 100:
    print('물의 상태는 기체입니다.')
elif 100 > temp > 0:
    print('물의 상태는 액체입니다.')
elif temp <= 0:
    print('물의 상태는 고체입니다.')
