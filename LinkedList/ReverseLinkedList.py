# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 머리가 텅 빈 경우
        if head==None:
            return None
            
        # 머리가 하나인 경우
        if head.next==None:
            return head
            
        # 그외
        M=L=ListNode()
        P=ListNode()
        P.next=head
        
        # 리스트에 하나씩 차곡차곡
        temp=[]
        c=-1
        while head:
            temp.append(head.val)
            head=head.next
        head=P.next
        
        # iter 무한으로 즐기면서 해당 번째 Linked 뽑기
        while -c<=len(temp):
            if temp[c]==head.val:
                temp[c]=head.val
                M.next=ListNode(head.val)
                M=M.next
                head=P
                c=c-1
            head=head.next
        return L.next
