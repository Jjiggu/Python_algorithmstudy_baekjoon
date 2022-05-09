# for i in range(1, 6):
#    for j in range(5-i):
#        print(' ', end="")
#    for j in range(1, i*2, 1):
#        print("*", end="")
#    print('')


n = int(input())
star = '*'
blank = ' '
stars = 1

for i in range(n, 0, -1):
    print(blank * (i - 1) + stars * star)
    stars += 2