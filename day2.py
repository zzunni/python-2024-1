print("==========================")
print("메뉴1번: 치즈버거")
print("메뉴2번: 치킨버거")
print("메뉴3번: 불고기버거")
print("==========================\n")

while True:
    menu_num = int(input("메뉴를 선택하세요: "))
    if menu_num == 1:
        print("치즈버거")
        break
    elif menu_num ==2:
        print("치킨버거")
        break
    elif menu_num ==3:
        print("불고기버거")
        break
    else:
        print("잘못 입력하셨습니다.\n")
        continue

