# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head):
            end=head
            prev=None
            curr=head
            while head:
                head=head.next
                curr.next=prev
                prev=curr
                curr=head
            return prev,end
        temp=head
        count=1
        sublists=[]
        lasthead=None
        while temp:
            
            if count==k:
                sublists.append(head)
                temp2=temp.next
                temp.next=None
                temp=temp2
                head=temp
                count=1
            count+=1
            if temp:
                temp=temp.next
             
        prev_end=ListNode()
        a=prev_end 
        for h in sublists:
            start,end=rev(h)
            prev_end.next=start
            prev_end=end
        prev_end.next=head
        return a.next

