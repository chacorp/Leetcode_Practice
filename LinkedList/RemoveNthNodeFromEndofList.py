# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # None인 경우
        if head.next==None:
            return head.next
            
        # 그 외...
        s=0
        L=ListNode()
        L.next=head
        
        # count length
        while head:
            s=s+1
            head=head.next
        
        # reset head
        head=L
        
        # iter 돌려서 해당 번째 건너뛰기
        for i in range(s-n+1):
            if i==s-n:
                head.next=head.next.next
            head=head.next
        return L.next
