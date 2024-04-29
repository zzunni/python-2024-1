info = input("주민번호 13자리 입력: ")

if int(info[6]) == 1 or int(info[6]) == 3:
    print("남자입니다.")

elif int(info[6]) == 2 or int(info[6]) == 4:
    print("여자입니다.")

