def calculate(radius):
    result = 3.141592 * radius ** 2
    return result

radius = int(input("반지름을 입력하시오: "))
result = calculate(radius)

print(f"반지름이 {radius}인 원의 면적은 {result}입니다.")