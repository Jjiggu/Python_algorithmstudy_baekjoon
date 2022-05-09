n, m = list(map(int, input().split()))
card = list(map(int, input().split()))

result = 0
length = len(card)

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = card[i]+card[j]+card[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)