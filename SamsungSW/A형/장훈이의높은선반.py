"""
0. 문제 설명 : B보다 높거나 같지만 제일 그중에서 제일 낮은 선반을 만들 때 그 차이를 출력하는 문제였다.

1. 풀이 방법 : 상당히 간단한 문제였다. 기본적으로 백트래킹, 혹은 이진 트리의 구조로 생각해서 매 순간 해당 index를 선택하면 그 키를 더해주고, 아니면 0을 더해주는 재귀의 방법으로 해결했다.
그런데 아마도 N이 20이하의 작은 범위라 가능했던 것 같다.
""" 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def check(cnt, sum):
    global answer, N, height
    if cnt == N:
        if (sum >= B):
            answer = min(answer, sum-B)
        return
    check(cnt + 1, sum)
    check(cnt+1, sum+height[cnt])
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    answer = sum(height) - B
    check(0, 0)
    print(f"#{test_case} {answer}")
     
    