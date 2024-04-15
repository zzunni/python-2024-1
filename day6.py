x = int(input(" 첫번째 수 = "))
y = int(input(" 두번째 수 = "))

max_value = (x if x>y else y)
min_value = (x if x<y else y)

print(f"큰 수 = {max_value}, 작은 수 = {min_value}")