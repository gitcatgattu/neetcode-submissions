# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        while list1 and list2:
            a,b=list1.val,list2.val
            if a<b:
                dummy.next=ListNode(a)
                list1=list1.next
            else:
                dummy.next=ListNode(b)
                list2=list2.next
            dummy=dummy.next
        dummy.next=list1 if list1 else list2
        return head.next
