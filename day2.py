a = int(input("시작값 입력: "))
b = int(input("끝값 입력: "))
c = int(input("증가값 입력: "))

sum = 0
for i in range(a,b,c):
    sum = sum + i
print(f"{a}부터 {b}까지 {c}씩 증가한 값의 합은 {sum}이다.")