num1, num2, num3 = map(int, input("점수 세개를 입력하세요: ").split())

my_score = int(input("내 점수를 입력하세요: "))
rank = 1

if my_score < num1:
    rank = rank+1

if my_score < num2:
    rank = rank+1

if my_score < num3:
    rank = rank+1

print(f"나의 등수는 {rank}입니다.")