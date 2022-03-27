"""
1. 문제 설명
- 하나의 행성에 대한 좌표를 (x, y, z)로 알려줄때 두 행성 사이의 거리는 dx, dy, dz의 최솟값이다.
- N-1개의 터널을 건설해서 모든 행성이 서로 연결되도록 할 때 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하시오
2. 풀이 방법
- MST를 구하는 문제였기 때문에 이를 위해 크루스칼 알고리즘을 구현하였다.
- 관건은 모든 인접한 엣지를 저장하면 메모리 초과가 발생하기 때문에 그러지 않고 
- x,y,z각각의 좌표별로 오름차순으로 정렬을 하고 1번째x좌표와 2번째 x좌표는 무조건 1번쨰 x좌표와 나머지 x좌표보다 거리가 짧을 것이기때문에 이 부분을 사용한다.
"""
import sys
input = sys.stdin.readline
def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)
    if x != y:
        parents[y] = x



N = int(input())
loc = []
for i in range(N):
    x, y, z = map(int, input().split())
    loc.append([x,y,z,i])
edge = [] 

for j in range(3):
    loc.sort(key = lambda x: x[j])
    before_idx = loc[0][3]
    for i in range(1, N):
        cur = loc[i][3]
        edge.append([abs(loc[i][j] - loc[i-1][j]), before_idx, cur])
        before_idx = cur
parents = [i for i in range(N+1)]
edge.sort(key = lambda x: x[0])
cnt = 0
cost = 0
for distance, a, b in edge:
    if find(a, parents) != find(b, parents):
        cost += distance
        cnt += 1
        union(a,b,parents)
    if cnt == N-1:
        break
                     
print(cost)

    
