N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for i in people: # c는 현재 사람
    rank = 1
    for j in people: # n은 다음 사람
        if (i[0] != j[0]) & (i[1] != j[1]): # i[0], j[0]은 몸무게, i[1], j[1]은 키
            if (i[0] < j[0]) & (i[1] < j[1]): # 둘 다 큰 경우
                rank += 1 # 순위 하나 증rk
    print(rank)