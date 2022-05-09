#괄호 입력 검사
def check(n):
    for i in range(n):
        arr = input()
        cnt = 0
        stack = []
        for j in range(len(arr)):
            if arr[j] == '(':
                stack.append(arr[j])
            else:
                if len(stack) == 0:
                    print("NO")
                    cnt = -1
                    break
                else:
                    stack.pop()
        if len(stack) == 0 and cnt == 0:
            print("YES")
        elif len(stack) != 0 and cnt == 0:
            print("NO")

# test case 개수 입력
n = int(input())
check(n)