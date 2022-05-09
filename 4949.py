while True:
    s = input()
    if s == '.':
        break
    stack = []
    temp = True
    for i in s:
        if i == '(' or i == '[': # 왼쪽 괄호를 만나면 스택에 삽입
            stack.append(i)
        elif i == ')': # ')'를 만나면 확인 후 스택에서 pop
            if not stack or stack[-1] == '[': # stack이 비어있거나 '['이면 flase로 바꾸고 break
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']': # ']'를 만나면 확인 후 스택에서 pop
            if not stack or stack[-1] == '(': # stack이 비어있거나 '('이면 flase로 바꾸고 break
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')



# [ first in ] ( first out )
# Half Moon tonight (At least it is better than no Moon at all].