# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k_nodes(temp,k):
            count=0
            while temp and count<k:
                temp=temp.next
                count+=1
            return count==k
        def reverse_k_nodes(head,k):
            prev=None
            curr=head
            for _ in range(k):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev,head,curr
        dummy=ListNode(0,head)
        prev_tail=dummy
        while has_k_nodes(prev_tail.next,k):
            new_head,new_tail,next_group=reverse_k_nodes(prev_tail.next,k)
            prev_tail.next=new_head
            new_tail.next=next_group
            prev_tail=new_tail
        return dummy.next
