self_num = set(range(1, 10001))
generated_num = set()
for i in range(1, 10001):
    for j in str(i): # 86 -> '8' '6' 으로 쪼갠다
        i += int(j) # 자리 수 더함 86 + 8 + 6
    generated_num.add(i) # 생성자 추가
self_num = self_num - generated_num # 셀프넘버만 남김
for i in sorted(self_num): # 순서대로 정
    print(i)