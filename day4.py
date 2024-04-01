def cal_score(*scores):
    total = 0
    num = len(scores)
    for score in scores:
        total = total + score

    print(f"총점: {total}점")
    print(f"평점: {total/num}점")

cal_score(90, 30, 80)



