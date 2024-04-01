def weeklypay(rate,hour):
    if hour>=30:
        pay = 30*rate + (hour-30)*rate*1.5
    else:
        pay = hour * rate

    return pay

rate = int(input("시급을 입력하세요: "))
hour = int(input("근무 시간을 입력하세요: "))

print(f"주급은 {weeklypay(rate, hour)}")