import sys

n = int(input())
check_li = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    check_li[num] = check_li[num] + 1

for i in range(10001):
    if check_li[i] != 0:
        for _ in range(check_li[i]):
            print(i)



