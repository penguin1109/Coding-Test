"""
0. 문제 설명 : a번의 학생의 키가 b번의 학생의 키보다 작으면 a에서 b로 방향을 갖는 방향 그래프를 작성한다.
자신의 키가 몇번째인지 알 수 있는 학생이 모두 몇명인지를 출력하여라

1. 풀이 방법
: 결국에 자신보다 크던 작던 노드끼리 연결이 된다면 그 경우에 자신의 등수를 알 수 있고 그래서 INF가 전혀 없으면 답이다.

2. 실패한 시도
: 처음에는 들어가는 노드와 나가는 노드가 모두 존재하면 반드시 자신의 순서를 알 수 있을 것이라고 생각했는데 틀렸다.

"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = 10**9
dp = [[INF]*(N+1) for _ in range(N+1)]
## 자기 자신으로의 거리는 0으로 변경
for i in range(1, N+1):
    dp[i][i] = 0

from collections import defaultdict
g_in = defaultdict(list)
g_out = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split()) ## a의 키가 b보다 작다.
    g_in[b].append(a)
    g_out[a].append(b)

def dfs(G, start):
    """_summary_
    depth first search
    Args:
        G (_defaultdict(list)_): _description_
        start (_integer_): _description_
    """
    import heapq
    q = [start]
    ret = 0
    while q:
        node = heapq.heappop(q)
        ret += 1
        for z in G[node]:
            if check[z] == 0:
                check[z] = 1
                heapq.heappush(q, z)
    return ret

def bfs(G, start):
    ret = 1
    for node in G[start]:
        if check[node] == 0:
            check[node] = 1
            ret += bfs(G, node)
    return ret

ans = 0

for i in range(1, N+1):
    check = [0]*(N+1)
    a = dfs(g_in, i)
    check = [0] * (N+1)
    b = dfs(g_out, i)

    if (a + b == N+1):
        ans += 1

print(ans)
    

