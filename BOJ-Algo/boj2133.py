import sys
input = sys.stdin.readline
n = int(input())
"""
1. 문제 설명 : 세로3, 가로 n인 공간에 2X1, 1X2크기의 타일을 깔고자 할 때에 경우의 수를 구하여라
2. 풀이 방법
: 모든 dp문제가 그렇듯이 점화식을 잘 구하면 되는 문제였다.
우선은 홀수개인 경우에는 답이 나올 수 없고, 따라서 N이 짝수인 경우들을 계산해서 구해주면 된다.
dp[0] = 1이고
dp[2] = 3이고 dp[4]는 dp[2] * dp[2] + dp[4-4] * 2(특이 케이스)로 구해준다.
나는 중복이라고 생각했던 부분이 중복이 아니었던 것이다.
그리고 N이 6인 경우에는 dp[6] = dp[6-2] * dp[2] + dp[6-4] * 2 + dp[6-6] * 2이렇게 해 주면 된다.
"""

def get_num(n):
    arr = [0] * (n+2)
    arr[2] = 3 # n이 2일때는 3개가 가능
    for i in range(4, n+1):
        if (i % 2 == 0):
            arr[i] = arr[i-2] * 3
            for j in range(i-4, -1,-2):
                arr[i] += arr[j] * 2
            arr[i] += 2

    return arr[n]

print(get_num(n))