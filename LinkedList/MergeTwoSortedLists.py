# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 둘 다 머리가 비었다면 암거나 리턴
        if l1 and l2 is None:
            return l1        
            
        # 그 외...
        l0=l=ListNode()
        
        # 현재 값 비교해서 낮은거 저장하고 저장한LL이랑 낮은 LL다음꺼로 돌리기 
        while l1 and l2:
            if l1.val <= l2.val:
                l0.next=l1
                l1=l1.next
            else:
                l0.next=l2
                l2=l2.next
            l0=l0.next
            
        # 루프 끝났는데 나머지 있는 거 걍 뒤에 붙이기
        if l2!=None:
            l0.next=l2
        else:
            l0.next=l1
        return l.next
            
