def cal_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    return sum

hap = cal_sum(100)
print(hap)