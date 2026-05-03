# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(l1,l2):
            dummy=ListNode()
            tail=dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next=l1
                    l1=l1.next
                else:
                    tail.next=l2
                    l2=l2.next
                tail=tail.next
            if l1:
                tail.next=l1
            if l2:
                tail.next=l2
            return dummy.next
        res=[]
        if len(lists)==0:
            return None
        new=lists[0]
        for i in range(1,len(lists)):
            new=merge_two(new,lists[i])
        return new
