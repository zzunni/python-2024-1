score = []

for i in range(5):
    score.append(int(input("성적을 입력하시오: ")))


total = 0
for i in score:
    total = total + i

mean = total/len(score)
score_sorted = sorted(score)  # 정렬된 리스트를 반환받습니다.

max = score_sorted[-1]  # 정렬된 리스트의 마지막 요소가 최대값입니다.
min= score_sorted[0]   # 정렬된 리스트의 첫 번째 요소가 최소값입니다.

num = 0
for i in score:
    if i >= 80:
        num = num+1

print(f"성적평균: {mean}")
print(f"최대점수: {max}")
print(f"최소점수: {min}")
print(f"80점이상: {num}")