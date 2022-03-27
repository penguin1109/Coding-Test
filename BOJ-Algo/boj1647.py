## 도시 분할 계획
import sys
input = sys.stdin.readline
import heapq

q = []
N, M = map(int, input().split())
for _ in range(M):
    A, B,C = map(int, input().split())
    heapq.heappush(q, (C, A, B))

def find_ancestor(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_ancestor(parent, parent[node])
    return parent[node]

def union(parent, node_a, node_b):
    a_ = find_ancestor(parent, node_a)
    b_ = find_ancestor(parent, node_b)
    
    if (a_ < b_):
        parent[b_] = a_
    else:parent[a_] = b_
    

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i


edge_count = 0
full_cost = 0
while q:
    temp = heapq.heappop(q)

    cost, a, b = temp[0], temp[1], temp[2]
    a_, b_ = find_ancestor(parent,a), find_ancestor(parent,b)
    
    if (a_ == b_):
        continue
    else:
        union(parent, a, b)
        edge_count += 1
        if (edge_count == N-1):
            break
        else:
            full_cost += cost
            
print(full_cost)

    