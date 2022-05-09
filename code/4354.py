import sys

def kmp(a):
    n = len(a)
    table = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]
        if a[i] == a[j]:
            j += 1
            table[i] = j
        return table

while 1:
    t = sys.stdin.readline().rstrip()

    if t == '.':
        break

    table = kmp(t)
    mod = len(t) - table[-1]

    if len(t) % mod == 0:
        print(len(t) // mod)

    else:
        print(1)

