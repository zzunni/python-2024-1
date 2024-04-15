

first = input("첫 번째 문자열: ")
second = input("두 번째 문자열: ")

ans = set(first) & set(second)

print("공통적인 글자:", end="")

for i in ans:
    print(i,end="")




