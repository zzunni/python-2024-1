def ct_to_ft(temp):
    ft = (temp-32.0)*5.0/9.0
    return ft
def ft_to_ct(temp):
    ct = temp*9.0/5.0 + 32
    return ct
def select_menu(num,temp):
    if num == 2:
        result = ct_to_ft(temp)
        print(f"화씨 온도는 {result}입니다.")
    else:
        result = ft_to_ct(temp)
        print(f"섭씨 온도는 {result}입니다.")


print("메뉴를 선택해주세요 \n 1. 화씨 -> 섭씨 \n 2. 섭씨 -> 화씨")
num = int(input(""))
temp = int(input("온도를 입력해주세요: "))

select_menu(num, temp)