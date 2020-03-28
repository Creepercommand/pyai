# 컴퓨터가 생각하는 수 구하기
# 기회는 6
# 6번 이후에는 정답을 입력한다
import random

ans = random.randint(1, 100)

for x in range(1, 7):
    a = input("찍어봐")
    if int(a) == ans:
        if x == 1:
            print("이걸 한방에?")
        else:
            print("와 정답")
        break
    else:
        if int(a) > ans:
            print("더 내려")
        else:
            print("더 올려")

if x == 6:
    print("틀림 정답은 %i" % ans)
