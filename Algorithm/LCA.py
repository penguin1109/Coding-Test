import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
LOG = 21 ## 2^20 = 1,000,000 (총 데이터가 백만개 들어올 수 있다는 가정)

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] ## 부모 노드의 정보
d = [0] * (n+1) ## 각 노드까지의 깊이
c = [0] * (n+1) ## 각 노드의 깊이가 계산되었는지의 여부
graph = [[] for _ in range(n+1)] ## 그래프의 정보

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b);graph[b].append(a);

## 루트 노드에서 시작해서 depth를 구한다.
def dfs(node, depth):
    c[node] = True;d[node] = depth
    for v in graph[node]:
        if c[v]:
            continue
        parent[v][0] = node ## 한칸 위의 부모에 대한 정보 저장 (2^0)
        dfs(v, depth+1)

# 전체 부모 관계 설정
def set_parent():
    dfs(1,0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 공통 조상 찾기
def lca(a,b):
    if (d[a] > d[b]):
        a,b = b,a
    ## 두 노드의 깊이를 맞춰 준다.
    for i in range(LOG-1, -1, -1):
        if d[b]-d[a] >= (2 ** i):
            b = parent[b][i]
    ## 부모가 동일해지도록
    if a==b: # 이미 부모가 같다면
        return a
    for i in range(LOG-1, -1, -1):
        ## 계속 윗 단계의 조상으로 거슬러 올라간다.
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0] ## 공통 조상 return

set_parent()
m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))