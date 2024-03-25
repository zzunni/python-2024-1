num1, num2, num3 = map(int, input("숫자 세개를 입력하세요: ").split())
max = num1

if max < num2:
    max = num2

if max < num3:
    max = num3

print(f"최대값은 {max}입니다.")