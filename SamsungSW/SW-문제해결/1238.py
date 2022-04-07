"""
0. 문제 설명 : 양벙향 연결 그래프 (from-to)가 주어질때 제일 마지막애 연락이 닿는 사람중 제일 큰 번호를 구하여라

1. 풀이 방법 : 누가 봐도 그래프 문제였고, 결국 순서라는 것이 dfs를 사용해서 트리에서의 깊이를 구하는 것이기 때문에 
heapq와 defaultdict를 사용해서 구하고 제일 큰 번호는 index를 사용해서 구했다.

"""

T = int(input())
from collections import defaultdict
import heapq

for test_case in range(1, T+1):
    length, start = map(int, input().split())
    graph = defaultdict(list)
    
    pairs = list(map(int, input().split()))
    for i in range(0, length-1,2):
        f, t = pairs[i], pairs[i+1]
        graph[f].append(t)
    visited = [-1 for _ in range(max(pairs) + 1)]

    q = [(0, start)]
    while q:
        step, node = heapq.heappop(q)
        visited[node] = step
        
        for n in graph[node]:
            if (visited[n] == -1):
                heapq.heappush(q, (step+1, n))
    
    answer = len(visited)-(visited[::-1].index(max(visited))+1)
    print(f"#{test_case} {answer}")
                
                
        
    
        