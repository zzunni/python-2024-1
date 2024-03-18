price = int(input("정가를 입력하시오: "))

if price >= 100:
    print("10층에서 사은품을 받아가세요.")
    saleprice = price * 0.85
    print(f"할인된 가격 = {saleprice}")

else:
    saleprice = price * 0.9
    print(f"할인된 가격 = {saleprice}")