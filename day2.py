price = int(input("가격을 입력하시오: "))
card = input("카드 종류를 입력하시오: ")

if price >= 30000 and card == "python":
    print("배송료가 없습니다.")

else:
    print("배송료는 3000원 입니다.")