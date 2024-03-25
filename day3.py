fruits = ['사과', '배', '딸기', '복숭아']

while True:
    input_fruit = input("사고싶은 과일은 무엇입니까? ")

    if  input_fruit in fruits:
        print(f"네. {input_fruit}가 있습니다.")
    elif input_fruit == '끝':
        print("안녕히 가십시오.")
        break

    else:
        print(f"지금 우리 가게에는 {input_fruit}이 없습니다.")
