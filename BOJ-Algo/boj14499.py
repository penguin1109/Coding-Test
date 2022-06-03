"""
BOJ14499. 주사위 굴리기 (시뮬레이션)
처음에는 주사위의 모든 면에 0이 존재한다.
크기가 MxN인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 지도의 좌표는 (r, c)로 나타낸다.
r = 북쪽으로부터 떨어진 칸의 개수, c = 서쪽으로부터 떨어진 칸의 개수
1. 이동한 칸에 있는 수가 0 -> 주사위 바닥에 있는 수가 칸에 복사됨
2. 이동한 칸에 있는 수가 0이 아닐때 -> 칸에 있는 수가 주사위 바닥면의 수가 되고 칸은 0이됨

입력 : 주사위를 놓은 곳의 좌표와 이동시키는 명령
출력 : 주사위가 이동했을 때 마다 주사위의 상단에 있는 값을 출력하여라
"""

import sys
input = sys.stdin.readline

N, M, x, y, K = list(map(int, input().split())) # 세로, 가로, 주사위 좌표, 명령 개수
dir_map = { 1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)} # 동 서 북 남

dice = [[0]*3 for _ in range(4)] # (0,1) (1,0) (1,1) (1,2) (2,1) (3,1)
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
#    print(board)

dir_orders = list(map(int, input().split()))

## 주사위의 전개도 상에서의 상단 하단 좌표는 계속 동일하게 하고 전개도를 바꾸자.
diceUx, diceUy = 0, 1 # 주사위의 상단의 전개도 상에서의 좌표
diceDx, diceDy = 2, 1 # 주사위의 하단의 전개도 상에서의 좌표


def changeDice(dir):
    if (dir == 1):
        px = [(0,1), (1,2), (2,1), (1,0)]
        temp = dice[0][1]
        dice[0][1] = dice[1][0]
        for i in range(1,4):
            p = px[i]
            cur = dice[p[0]][p[1]]
            dice[p[0]][p[1]] = temp
            temp = cur
    elif (dir == 2):
        px = [(0,1),(1,0),(2,1),(1,2)]
        temp = dice[0][1]
        dice[0][1] = dice[1][2]
        for i in range(1, 4):
            p = px[i]
            cur = dice[p[0]][p[1]]
            dice[p[0]][p[1]] = temp
            temp = cur
    elif (dir == 3 or dir == 4):
        newcol = []
        if (dir == 4):
            px = [(3,1), (0,1), (1,1), (2,1)]
        else:
            px = [(1,1), (2,1), (3,1), (0,1)]
        for i in range(4):
            p = px[i]
            newcol.append(dice[p[0]][p[1]])
        for i in range(4):
            dx, dy = i, 1
            dice[dx][dy] = newcol[i]


for k in range(K):
    dir = dir_orders[k]
    valid = False
    if (dir == 1): # 동쪽으로 이동하는 경우
        nx, ny = x, y+1
        if (0 <= nx < N and 0 <= ny < M): # 명령이 유효한 경우
            x = nx;y = ny;valid = True;
            changeDice(dir)
            num = board[x][y]
            if (num == 0):
                board[x][y] = dice[diceDx][diceDy] # 지도의 수가 0이기 때문에 주사위 하단의 수를 복사해 준다.
            else:
                dice[diceDx][diceDy] = board[x][y]
                board[x][y] = 0
    elif (dir == 2): # 서쪽으로 이동하는 경우
        nx, ny = x, y-1
        if (0 <= nx < N and 0 <= ny < M):
            x = nx;y = ny;valid = True;
            changeDice(dir)
            num = board[x][y]
            if (num == 0):
                board[x][y] = dice[diceDx][diceDy]  # 지도의 수가 0이기 때문에 주사위 하단의 수를 복사해 준다.
            else:
                dice[diceDx][diceDy] = board[x][y]
                board[x][y] = 0
    elif (dir == 3): # 북쪽으로 이동하는 경우
        nx, ny = x-1, y
        if (0 <= nx < N and 0 <= ny < M):
            x = nx;y = ny;valid = True;
            changeDice(dir)
            num = board[x][y]
            if (num == 0):
                board[x][y] = dice[diceDx][diceDy]  # 지도의 수가 0이기 때문에 주사위 하단의 수를 복사해 준다.
            else:
                dice[diceDx][diceDy] = board[x][y]
                board[x][y] = 0
    else:
        nx, ny = x + 1, y
        if (0 <= nx < N and 0 <= ny < M):
            x = nx;y = ny;valid = True;
            changeDice(dir)
            num = board[x][y]
            if (num == 0):
                board[x][y] = dice[diceDx][diceDy]  # 지도의 수가 0이기 때문에 주사위 하단의 수를 복사해 준다.
            else:
                dice[diceDx][diceDy] = board[x][y]
                board[x][y] = 0
    if valid:
        print(dice[diceUx][diceUy])



