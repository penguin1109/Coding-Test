## NQueen 문제
"""
NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하여라
알고리즘 : 백트래킹
-> 문제는 pypy3 으로 실행했을 때에만 시간 초과가 나지 않는다는 것이다.
"""
N = int(input()) # 체스판의 크기
ck = [[0]* N for _ in range(N)]

answer = 0
import math
def check_valid(x, y):
    ## 가로 / 세로 방향 확인
    for i in range(x):
        if ck[i][y] == 1:
            return False
    ## 대각선 확인
    for i in range(x):
        for j in range(N):
            if ck[i][j] == 1 and (abs(i-x) == abs(j-y)):
                return False
    return True

def nqueen(i):
    global answer
    if i == N:
        answer += 1
        return
    for j in range(N):
        if ck_row[j] == -1:
            valid = True
            for m in range(i): ## 가로 열 인덱스
                if (abs(j-ck_side[m]) == abs(m-i)): ## 같은 대각선상에 존재하면
                    valid = False
                    continue
            if valid:
                ck_row[j] = 0;ck_side[i] = j;
                nqueen(i+1) ## 재귀 호출
                ck_row[j] = -1;ck_side[i] = -1; ## 원상 복귀

for i in range(N):
    ck_row = [-1]*N;ck_side = [-1]*N;
    ck_row[i] = 0;ck_side[0] = i;
    nqueen(1)
print(answer)