num = int(input("원하는 단은: "))
time = 1

while time <= 9:
    for i in range(1,10):
        print(f"{num} * {i} = {num*i}")
        time=time+1