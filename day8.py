a = input("문자열을 입력하시오: ")

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(len(a)):
    if a[i].isdigit() == True:
        sum1 +=1

    elif a[i].isspace() == True:
        sum2 +=1

    elif a[i].isalpha() == True:
        sum3 +=1

info = {"digit":sum1, "spaces":sum2, "alpha":sum3}
print(info)