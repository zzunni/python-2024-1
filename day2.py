num = int(input("정수를 입력하시오: "))

fact = 1
for i in range(num,0,-1):
    fact = fact * i

print(f"{num}!은 {fact}이다.")