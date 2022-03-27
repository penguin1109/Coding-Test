"""
0. 집 구하기
1. 문제 설명
- 맥세권 : 맥도날드와 집 사이의 최단 거리가 x이하인 집
- 스세권 : 스벅과 집 사이의 최단 거리가 y이하인 집
- 맥세권과 스세권을 만족하는 집 중 최단거리의 합이 최소인 집을 구하여라
"""
"""
import sys
input = sys.stdin.readline
INF = 10**4

V, E = map(int, input().split())
from collections import defaultdict
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    ## 다른 두 정점 사이에 여러개의 간선이 존재할 수 있다.
    graph[u].append((w,v))
    graph[v].append((w, u))
    
    
def dikstra(start, graph):
    D = [INF for i in range(V+1)]
    visited = [False] * (V+1)
    D[start] = 0
    import heapq
    q = [(0, start)]
    while q:
        temp = heapq.heappop(q)
        cost, node = temp[0], temp[1]
        visited[node]=True
        for edge in graph[node]:
            c,n = edge[0], edge[1]
            if (visited[n] == False):
                D[n] = min(D[n], c + cost)
                heapq.heappush(q, (D[n], n))
    return D


M, x = map(int, input().split())
mac = list(map(int, input().split())) # 맥도날드의 정점
S, y = map(int, input().split())
star = map(int, input().split()) # 스타벅스의 정점

home = [0] * (V+1)

for m in mac:
    d = dikstra(m, graph)
    for idx, dist in enumerate(d):
        if (dist != 0 and dist <= x):
            if (home[idx] == 0):
                home[idx] =  dist
            else:
                home[idx] = min(home[idx], dist)
answer = INF

for s in star:
    d = dikstra(s, graph)
    for idx, dist in enumerate(d):
        if (dist!=0 and dist <= y and home[idx] != 0):
            answer = min(answer, home[idx] + dist)

if (answer == INF):
    print(-1)
else:
    print(answer)
"""

import sys
input = sys.stdin.readline
INF = 10**9
V, E = map(int, input().split())
from collections import defaultdict
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    ## 다른 두 정점 사이에 여러개의 간선이 존재할 수 있다.
    graph[u].append((w,v))
    graph[v].append((w, u))
    
M, x = map(int, input().split())
mac = list(map(int, input().split())) # 맥도날드의 정점
S, y = map(int, input().split())
star = map(int, input().split()) # 스타벅스의 정점

mnode, snode = V+1, V+2
for m in mac:
    graph[mnode].append((0,m))
    graph[m].append((0, mnode))
for s in star:
    graph[snode].append((0, s))
    graph[s].append((0, snode))


mdist = [INF for i in range(V+3)]
mdist[mnode] = 0
sdist = [INF for i in range(V+3)]
sdist[snode] = 0

def dikstra(start, dist):
    q = [(0,start)]
    while q:
        cost, node = heapq.heaappop(q)
        if (dist[node] < cost):continue
        for c, n in graph[node]:
            if (n == snode or n == mnode):
                continue
            if (cost + c < dist[node]):
                dist[node] = cost + c
                heapq.heappush(q, (dist[node], n))

dikstra(mnode, mdist)
dikstra(snode, sdist)

answer = INF
for i in range(1, V+1):
    if (i in mac) or (i in star):
        continue
    if (mdist[i] <= x and sdist[i] <= y):
        if (mdist[i] + sdist[i] < answer):
            answer = mdist[i] + sdist[i]
if answer == INF:
    print(-1)
else:
    print(answer)