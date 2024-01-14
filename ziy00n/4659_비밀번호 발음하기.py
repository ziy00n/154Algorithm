# 백준 4659_비밀번호 발음하기
# 자료구조

import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input().rstrip()
    if pw == 'end':
        break
    v_cnt = 0 # 모음 갯수
    v_repeat = 0 # 연속 모음 갯수
    c_repeat = 0 # 연속 자음 갯수
    last = '' # 직전 문자
    flag = True # 조건 만족 여부
    
    for i in pw:
        if i in vowel: # 모음일 때
            if v_repeat == 2 or ((i != 'e' and i != 'o') and last == i): # 모음 3개 연속(조건2 X) Or (e, o 가 아니면서 직전 문자와 같은 모음(조건3 X)
                flag = False
                break
            else:
                v_repeat += 1
                c_repeat = 0
                v_cnt += 1
                last = i
        else: # 자음일 때
            if c_repeat == 2 or last == i: # 자음 3개 연속(조건2 X) Or 직전 문자와 같은 자음(조건3 X)
                flag = False
                break
            else:
                c_repeat += 1
                v_repeat = 0
                last = i
    if v_cnt == 0: # 모음 없을 때 (조건1 X)
        flag = False

    if flag:
        print("<"+ pw +"> is acceptable.")
    else:
        print("<{}> is not acceptable.".format(pw))