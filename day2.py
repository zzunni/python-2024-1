grade = float(input("학점은? "))
toeic = int(input("토익점수는? "))

if grade >= 4.0 and toeic >= 800:
    print("장학금을 받을 수 있습니다.")

else:
    print("이번 학기는 장학금을 받을 수 없습니다.")