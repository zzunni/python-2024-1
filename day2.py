born_date = int(input("출생년도 끝자리 입력: "))
age = int(input("만 나이를 입력하세요: "))

if age >= 65:
    print("언제든지 구매 가능합니다.")
else:
    if born_date == 1 or born_date == 6:
        print("월요일에 구매 가능합니다.")
    elif born_date == 2 or born_date == 7:
        print("화요일에 구매 가능합니다.")
    elif born_date == 3 or born_date == 8:
        print("수요일에 구매 가능합니다.")
    elif born_date == 4 or born_date == 9:
        print("목요일에 구매 가능합니다.")
    else:
        print("금요일에 구매 가능합니다.")