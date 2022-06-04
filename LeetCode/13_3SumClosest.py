import math

class Solution:
    """
    Input  : 길이가 n인 정수 배열, target
    Output : target과 가장 유사한 숫자들의 합
    
    Solution :
    1. 인접한 3개의 숫자들의 합일 필요는 없기 때문에 sliding window는 의미가 없다.
    2. 사용해 볼 수 있는 알고리즘으로는 이럴때는 보통 dp나 모든 경우를 시도해보는 back tracking가 제일 많이 사용되는 것 같다.
    3. 3중 for문을 사용했더니 예상은 했으나 시간 초과가 발생하였다. 그렇다면 two pointer을 시도해 보면 어떨까? (그런데 음수가 섞여 있다.)
        3-1. 부분 배열 합이 target보다 작으면 end + 1
        3-2. 부분 배열 합이 target보다 크면 start + 1
    """
    def bestSol(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        N = len(nums)
        for i in xrange(N):
            l, r = i+1, N-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: # break early 
                return res
        return res
    def threeSumClosest(self, nums, target):
        answer = 0
        N = len(nums)
        best = 1000000000
        ## 결국에는 target과 "가까운"보다는 target과 "같은" 합이 되는 3개의 숫자 조합을 찾는 것이 관건이다.
        if N >= 3:
            nums.sort() ## 오름차순 정렬
            for i in range(N-2): ## mid index를 변경해 줌
                if (i > 0 and nums[i] == nums[i-1]):continue
                start, end = i + 1, N - 1 ## mid의 왼쪽, 마지막 원소
                while (start < end):
                    add = nums[start] + nums[end] + nums[i]
                    if (abs(add-target) < best):
                        best = abs(add-target) ## 이부분에서 best갱신을 잊어서 계속 틀렸다고 나왔었다.
                        answer = add ## answer 갱신
                    if (add < target):
                        start += 1 ## 더 작으면 키워주자 
                    elif (add > target):
                        end -= 1 ## 더 크면 줄여주자
                        
                    else: ## (add == target) -> early break
                        return target
        return answer
                    
                        

        
    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ## 순서가 상관없으니 정렬해도 상관없지 않을까?
        best = 100000000
        answer = 0
        nums = sorted(nums) # [-4, -1, 1, 2]
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    add = nums[i] + nums[j] + nums[k]
                    if (abs(add-target) < best):
                        best = abs(add-target)
                        answer = add
                        if (best == 0):
                            return answer
        return answer
                        
                        
                    
                
