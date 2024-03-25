import random

answer = random.randint(1,100)
print("1부터 100까지의 숫자를 맞추시오")

while True:
    input_ans = int(input("숫자를 입력하시오:"))
    if input_ans < answer:
        print("너무 낮음!")
    elif input_ans > answer:
        print("너무 높음!")
    else:
        print("축하합니다.")
        break

