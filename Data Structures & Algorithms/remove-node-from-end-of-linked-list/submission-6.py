# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        for i in range(n):
            temp=temp.next
        if not temp:
            return head.next
        prev=head
        while temp and temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=prev.next.next 
        return head