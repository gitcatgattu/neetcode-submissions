# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp=head
        count=1
        while temp.next:
            temp=temp.next
            count+=1
        if count==1:
            return None
        elif count==2 and n==1:
            head.next=None
            return head
        elif count==2 and n==2:
            return head.next
        elif count==3 and n==1:
            head.next.next=None
            return head
        elif count==3 and n==2:
            head.next=head.next.next
            return head
        elif count==3 and n==3:
            return head.next

        if count==n:
            return head.next

        c=count-n-1
        t=head
        while c>=1:
            t=t.next
            c-=1
        t2=t.next.next
        t.next=t2
        return head