M, N = map(int, input().split())
#li에 입력받은 체스판 저장
li = []
for i in range(M):
    li2 = list(input())
    li.append(li2)

li3 = []
#k와 l은 검사를 시작하는 시작
for k in range(0, M-7):
    for l in range(0, N-7):
        #WBWB로 시작
        count1 = 0
        for i in range(k, 8+k):
            for j in range(l, l+8):
                if (i + j) % 2 == 0:
                    if li[i][j] != 'W':
                        count1 += 1
                else:
                    if li[i][j] != 'B':
                        count1 += 1
        li3.append(count1)
    #BWBW로 시작
        count2 = 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                if (i + j) % 2 == 0:
                    if li[i][j] != 'B':
                        count2 += 1
                else:
                    if li[i][j] != 'W':
                        count2 += 1
        li3.append(count2)
#print(li3)
print(min(li3))