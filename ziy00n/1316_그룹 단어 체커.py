# 1316_그룹 단어 체커
# implementation

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    flag = True
    for i in range(len(word)-1) : # 단어의 인덱스0부터
        if word[i] != word[i+1] : # 현재 알파벳이 다음 문자와 같지 않을 때
            if word[i] in word[i+1:] :  # 다음 문자들 중에 있으면
                flag = False
                break
    if flag == True:
        cnt += 1
        
print(cnt)