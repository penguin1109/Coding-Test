"""
BOJ 3184. 양
- 사용해야 하는 알고리즘 : BFS
- '.' : 빈 필드 '#' : 울타리 'o' : 양 'v' : 늑대
- 한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면 두 칸은 같은 영역 안에 속해 있다고 한다.
- 마당에서 탈출 할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.
- 살아남은 양과 늑대의 수를 구하여라
- 같은 영역에서 늑대 >= 양 : 양 = 0   늑대 < 양 : 늑대 = 0
- 탈출 가능한 영역이면 계산 안함
"""
import sys
input = sys.stdin.readline

def bfs(i,j, g):
    dx,dy = [-1, 1, 0, 0], [0,0,-1,1]
    wolf = sheep = 0
    if (field[i][j] == 'v'):wolf += 1
    elif (field[i][j] == 'o'):sheep += 1
    q = [(i,j)]
    while (q):
        temp = q.pop(0)
        i,j = temp[0], temp[1]
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]

            if (0 <= ni < R and 0 <= nj < C):
                if (field[ni][nj] != '#' and visit[ni][nj] == False):
                    if (field[ni][nj] == 'v'):
                        wolf += 1
                    elif (field[ni][nj] == 'o'):
                        sheep += 1
                    group[ni][nj] = g
                    visit[ni][nj] = True
                    q.append((ni,nj))
            else:
                return 0,0
    if (wolf >= sheep):
        sheep = 0
    else:
        wolf = 0
    return wolf, sheep


R, C = map(int, input().split())
field = [[] for _ in range(R)]
for i in range(R):
    row = str(input()).strip()
    for j in range(len(row)):
        field[i].append(row[j])

visit = [[False] * C for _ in range(R)]
g = 1
all_w, all_s = 0,0
group = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if (visit[i][j] == False and field[i][j] != '#' and group[i][j] == 0):
            visit[i][j] = True;group[i][j] = g;
            w,s = bfs(i,j, g)

            all_w += w;all_s += s;
            g += 1
print(f"{all_s} {all_w}")



