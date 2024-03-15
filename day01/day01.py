'''
r=5
h=10
pi = 3.141592

v = pi * r*r * h
print("{:.1f}".format(round(v)))'''

'''name = input()
print(f"{name}씨, 안녕하세요?")
print("파이썬에 오신걸 환영합니다.")'''


# a = int(input("수학점수를 입력하시오: "))
# b = int(input("영어점수를 입력하시오: "))
# c = int(input("국어점수를 입력하시오: "))
# sum = a+b+c
# mean = sum/3
# print(f"당신의 중간고사 평균점수는 {mean}점 입니다.")

# a = int(input("첫번째 점수를 입력하시오: "))
# b = int(input("두번째 점수를 입력하시오: "))
# print(f"{a}+{b}={a+b}")
# print(f"{a}-{b}={a-b}")
# print(f"{a}*{b}={a*b}")
# print(f"{a}/{b}={a/b}")

# r = int(input("반지름을 입력하시오: "))
# print(f"반지름이 {r}인 원의 넓이={3.14159*r*r:.2f}")
# print(f"반지름이 {r}인 원의 넓이={3.14159*r*r}")

# price = 12345
# tax = price * 0.075
# tax = round(tax, 2)
# print(tax)

# F = int(input("화씨온도를 입력하시오: "))
# print(f"섭씨온도: {(F-32)*5/9:.2f}")

# w = float(input("몸무게(kg)를 입력하시오: "))
# h = float(input("키(m)를 입력하시오: "))
# bmi = w/(h*h)
# print(f"당신의 BMI 지수는: {bmi:.2f}")

# import math
# a = int(input("빵의 개수를 입력하시오: "))
# print(f"빵을 나누어줄 수 있는 최대인원:{math.floor(a/3)} \n남은 빵 개수:{a%3}")

# a = (24*(1+0.08)**382)
# print(f"{a}")

# a = int(input("물건값을 입력하시오: "))
#
# b = int(input("1000원 지폐개수:"))
# c = int(input("500원 동전개수:"))
# d = int(input("100원 동전개수:"))
#
# M=1000*b+500*c+100*d-a
#
# print(f"500원:{int(M/500)} 100원:{int(M/500/100)} 10원:{int(M/500/100/10)} "
#       f"1원:{int(M/500/100/10/1)}")

# a = int(input("나이를 입력하시오: "))
# if a<15:
#     print("15세가 안되었군요~ 입장불가입니다.")
# else:
#     print("끝")

# a = int(input("5의 배수를 입력하시오: "))
# if a%5==0:
#     print("5의 배수를 입력하셨습니다.")
# else:
#     print("5의 배수를 입력하지 않으셨습니다.")

'''실습2/3'''
# a = int(input("첫번쨰 점수를 입력하시오: "))
# b = int(input("두번쨰 점수를 입력하시오: "))
# c = int(input("세번쨰 점수를 입력하시오: "))
# mean = int((a+b+c)/3)
# if mean>=60:
#     print("축하합니다 합격입니다.")
# else:
#     print("아쉽지만 불합격입니다.")

id = "python"
a = input("아이디를 입력하시오: ")

if id == a:
    print("환영합니다.")
else:
    print("아이디를 찾을 수 없습니다.")