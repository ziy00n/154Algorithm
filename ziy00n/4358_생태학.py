# 백준 4358_생태학
# 자료구조

from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int) # 초기값 0으로 설정되는 딕셔너리
tree_cnt = 0 # 전체 나무 수

while True:
    tree = input().rstrip()
    if tree == '':
        break
    tree_cnt += 1 # 나무 이름별 value값에 +1
    trees[tree] += 1 # 총 나무 수 +1

trees_list = list(trees.keys()) # 나무이름(=key값들) 리스트로 저장
trees_list.sort() # 오름차순 정렬

for tree in trees_list:
    print('%s %.4f' %(tree, (trees[tree]/tree_cnt)*100)) 