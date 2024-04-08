blood = []

while True:
    blood.append(input("혈액형을 선택하세요(A,B,AB,O): "))
    print("헌혈해주셔서 감사합니다. ")

    print("--------------------")
    print(f"A형: {blood.count('A')}")
    print(f"B형: {blood.count('B')}")
    print(f"AB형: {blood.count('AB')}")
    print(f"O형: {blood.count('O')}")

    command = input("입력을 계속할까요?(Yes/No): ")

    if command == 'Yes':
        continue

    elif command == 'No':
        break