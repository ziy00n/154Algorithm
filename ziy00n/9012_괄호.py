# 백준 9012_괄호
# 자료구조 - 스택

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack=[]
    ps = input()
    for i in ps :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) != 0:
                stack.pop()
            else :
                print("NO")
                break
    else :
        if len(stack) == 0:
            print("YES")
        else :
            print("NO")