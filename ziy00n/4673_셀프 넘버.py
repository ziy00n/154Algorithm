# 백준 4673_셀프 넘버
# implementation

# 차집합 연산을 위해서 set자료형 사용
natural_num = set(range(1,10001)) # 1 ~ 10000 자연수
generated_num = set() # 생성자로 생겨난 숫자들

for i in range(1, 10001): # i는 생성자
    for j in str(i):
        i += int(j) # 이때 i는 생성자로 생겨난 d(n)
    generated_num.add(i)

# 셀프 넘버 = 전체 자연수 - generated_num
self_num = sorted(natural_num - generated_num)

for i in self_num:
    print(i)