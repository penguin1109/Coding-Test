"""
0. 문제 설명 : 입국심사를 할 수 있는 심사대의 개수와 심사를 받아야 하는 사람의 수, 
그리고 각 심사대에서 걸리는 시간이 주어질때 모두가 심사를 받기 위한 최소의 시간은?

1. 풀이 방법 : 
처음에는 그리디를 사용해서 풀어야 한다고 생각하고 heapq를 사용해서 계속 빨리 끝나는 순서대로 넣으려 했다.
그러나 그렇게 했을 때 수행 시간에 따른 차이가 있었기 때문에 reverse binary search를 사용하였다.
총 걸릴 수 있는 시간의 하한선을 정하고 해당 시간에 대해 모든 심사 시간을 나눈 것의 합이 인원수를 초과하는 경우에
하한을 mid+1로 올려주고 인원수보다 작으면 상한을 mid-1로 내려준다.
이렇게 상한과 하한이 수렴하면 그때 하한이 최소니까 답이다.
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
import heapq
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    time =[] # 각 심사대에서 심사에 걸리는 시간
    for _ in range(N):
        time.append(int(input()))
    Range = max(time) * M
    time.sort(reverse = False)
    left, right= 0, Range+1
    min_time = 10**9
    while (left <= right):
        mid = (left+right)//2
        add = 0
        for i in range(N):
            add += mid // time[i]
        if (add >= M):
        	right = mid-1
        else:left = mid+1
    print(f"#{test_case} {left}")       
        
    