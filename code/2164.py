a = int(input())
n = [i for i in range(1, a+1)]

while len(n) > 1: # 리스트에 요소가 하나만 남을 때까지
    n.pop(0)
    n.append(n[0])
    n.pop(0)

print(n[0]) 