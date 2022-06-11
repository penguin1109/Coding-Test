"""
1248. 공통 조상
- 이진 트리에서 임의의 두 정점의 공통 조상 중 가장 가까운 것을 찾으려 한다.
- 임의의 이진 트리가 주어지고, 두 정점이 명시 될 때 이들의 공통 조상중 (1) 가장 가까운 정점과 (2) 그 정점을 루트로 하는 서브 트리의 크기를 알아 내어라
- 자식 정점이 부모 정점의 왼쪽 자식인지 오른쪽 자식인지는 중요하지 않다.
"""


def dfs(node, depth):
    """

    :param node: 현재 방문하는 노드
    :param depth: 현재 방문하는 노드의 깊이
    :return: 재귀적으로 동작하는 함수이다. 깊이 우선 탐색을 함으로서 각각의 노드들의 그래프에서의 높이 정보를 갱신 할 수 있다.
    """
    check[node] = True;
    depths[node] = depth;
    for n in graph[node]:
        if (check[n] == False):
            parent[n][0] = node
            dfs(n, depth + 1)


def set_parent():
    dfs(1, 0) ## 기본적으로 사용이 되는 이진 트리에서 루트 노드가 1이고 번호아 0이라고 했음
    for i in range(1, LOG):
        for j in range(1, V + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b):
    if (depths[a] > depths[b]):
        a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if (depths[b] - depths[a]) >= 2 ** i:  # b와 a의 높이가 같지 않을 때
            b = parent[b][i]
    if (a == b):
        return a
    for i in range(LOG - 1, -1, -1):
        if (parent[a][i] != parent[b][i]):
            a = parent[a][i];
            b = parent[b][i];
    return parent[a][0]


def tree_size(root):
    q = [root]
    cnt = 0
    ck = [False] * (V + 1)
    while q:
        temp = q.pop(0)
        ck[temp] = True
        cnt += 1
        for g in graph[temp]:
            if ck[g] == False:
                q.append(g)

    return cnt


LOG = 21
T = int(input())  # 테스트 케이스 개수
for t in range(T):
    info = list(map(int, input().split()))
    V, E, a, b = int(info[0]), int(info[1]), int(info[2]), int(info[3])  ## 정점의 개수, 간선의 개수, 공통 조상을 찾는 두 정점의 번호

    nodes = list(map(int, input().split()))
    graph = [[] for _ in range(V + 1)];
    parent = [[0] * LOG for _ in range(V + 1)];
    depths = [0] * (V + 1);
    check = [False] * (V + 1);
    for e in range(0, len(nodes), 2):
        p, c = nodes[e], nodes[e + 1]  ## parent => child
        graph[p].append(c)
    set_parent()
    same_p = lca(a, b)
    size = tree_size(same_p)
    print(f"#{t + 1} {same_p} {size}")









