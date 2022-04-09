"""
0. 문제 설명
스타크래프트에서 벙커를 찾기 위해서는 배럭을 먼저 지어야 하고 여러개의 건물을 동시에 지을 수 없다.
N개의 각 건물이 완성되기까지 걸리는 최소 시간을 출력하여라

"""
import sys
input = sys.stdin.readline
N = int(input())
from collections import defaultdict
buildT = []
preT = defaultdict(list)
parent = defaultdict(list)
in_degree = [0 for _ in range(N)]
for _ in range(N):
    info = list(map(int, input().split()))
    buildT.append(info[0])
    for i in range(1, len(info)-1):
        preT[_+1].append(info[i])
        in_degree[_] += 1 ## 정점에 들어오는 간선의 수를 저장
        parent[info[i]].append(_+1) # 부모 저장
import heapq
start = in_degree.index(0) +1
q = [start]
dp = [0] + buildT

while (q):
    node = heapq.heappop(q)
    for p in parent[node]:
        if (in_degree[p-1] > 0):
            in_degree[p-1] -= 1
            dp[p] = max(dp[p], dp[node] + buildT[p-1])
            heapq.heappush(q, p)
print(dp)
