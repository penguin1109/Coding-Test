# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. linked list가 주어졌을 때 모든 두개의 인접 노드를 swap하고 head를 return 하여라.
        1->2->3->4
        2->1->3->4 (head : 1 tmp : 2)
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp (현재 swap된 ListNode의 head를 반환)
      return head (만약에 head.next나 head가 None이었다면 head를 그냥 반환한다. swapping하는 액션이 필요가 없기 때문이다.)
        2->1->4->3 (head : 3 tmp : 4)
    2. 적용 알고리즘 : 재귀 / 연결 리스트
    3. recursive과 iterative는 무조건 동시에 구현 가능할 줄 알아야 한다. 처음에 생각한 솔루션은 재귀적인 구조였지만 이를 iterative하게 구현하려 하니 dummy node를 앞에 추가할 생각을 못했기 때문에 
    까다로웠다. 
    """
    
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Recursive Version
        
        if head and head.next:
            # head -> tmp 
            tmp = head.next ## 인접한 다음 노드
            head.next = self.swapPairs(tmp.next)
            tmp.next = head ## head와 다음 노드인 temp와 위치 변경
            return tmp
            # head = tmp## 위치 변경 tmp -> head
            
        return head
    
    def swapPairs(self, head):
        ## Iterative Version
        
        nullHead = p = ListNode(0)
        nullHead.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            ## p 갱신 
            p.next = tmp
            head = head.next ## 새로운 head로 변경
            p = tmp.next ## 새로운 head 직전의 node
        return nullHead.next
        
            
            
