a = input("문자열을 입력하시오: ")

new_A = a.split()

for i in new_A:
    print(i[0].upper(),end= '')
