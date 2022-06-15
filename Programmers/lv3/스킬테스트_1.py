answer = 0
class Node(object):
    def __init__(self, key, left, right):
        self.left = left ## left node index
        self.right  = right ## right node index
        self.key = key

def solution(sticker):
    global answer
    def make_idx(idx):
        l,r = idx-1, idx+1
        if (l < 0):
            l = len(sticker)-1
        if (r >= len(sticker)):
            r = 0
        return l, r
    """
    원형의 스티커 하나를 뜯으면 좌우에 있는 스티커도 모두 사용이 불가능하다.
    스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return하는 함수를 완성하여라.
    원형 배열의 첫번째 원소와 마지막 원소가 서로 연결되어 있다.
    """
    dp = [[0]*2 for _ in range(len(sticker))]
    ## dp[i][0] : i번째 선택 안했을 때의 최대 합
    ## dp[i][1] : i번째 선택 했을 때의 최대 합
    dp[0][1] = sticker[0]
    for i in range(1, len(sticker)):
        l, r = make_idx(i)
        dp[i][0] = max(dp[l][0],dp[l][1])
        if (i == 1):
            dp[i][1] = sticker[i] + dp[0][0]
        if (i == len(sticker)-1):
            dp[i][1] = 0
        else:
            dp[i][1] = max(dp[l][0], dp[i-2][1], dp[i-2][0]) + sticker[i]
    for i in range(len(dp)):
        answer = max(dp[i][0], dp[i][1], answer)
    dp = [[0]*2 for _ in range(len(sticker))]
    ## 첫번째 선택 안 함

    for i in range(1, len(sticker)):
        l, r = make_idx(i)
        dp[i][0] = max(dp[l][0],dp[l][1])
        if (i == 1):
            dp[i][1] = sticker[i] + dp[0][0]
        else:
            dp[i][1] = max(dp[l][0], dp[i-2][1], dp[i-2][0]) + sticker[i]
    for i in range(len(dp)):
        answer = max(dp[i][0], dp[i][1], answer)
    # print(dp)
    return answer
