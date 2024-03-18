express_point = input("배송지(현재는 korea와 us만 가능): ")
price = int(input("상품의 가격: "))

if express_point == "korea":
    if price >= 20000:
        print("배송비 = 0")
    else:
        print("배송비 = 3000")

else:
    if price >= 100000:
        print("배송비 = 0")
    else:
        print("배송비 = 8000")