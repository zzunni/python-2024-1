command = ""
total = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    command = input("계속?(yes/no): ")
    total = total + num
    if command == "no":
        break

print(f"합계는 {total}")
