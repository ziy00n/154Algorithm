# 백준 11656_접미사 배열
# 문자열

import sys
input = sys.stdin.readline

S = input().rstrip()
S_list = []

for _ in S:
    S_list.append(S) # 맨 앞 글자 뺀 문자열 저장
    S = S[1:] # 맨앞글자 제외하고(인덱스0) 끝까지의 문자열

S_list.sort() # 알파벳 순 정렬

for i in S_list:
    print(i)