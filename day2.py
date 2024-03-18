today_num = int(input("오늘날짜(숫자입력): "))
car_num = int(input("차량번호 4자리를 입력하세요: "))

if today_num % 2 == 0:
    print("오늘은 짝수차량 입장가능.")
    if car_num % 2 == 0:
        print("귀하의 차량은 입차 가능합니다.")
    else:
        print("귀하의 차량은 입차 불가합니다.")
else:
    if car_num % 2 == 0:
        print("귀하의 차량은 입차 불가합니다.")
    else:
        print("귀하의 차량은 입차 가능합니다.")