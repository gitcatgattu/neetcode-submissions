# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.front = head
        
        def recurse(node):
            if not node:
                return True  # reached end
            
            # Go to the end first
            if not recurse(node.next):
                return False
            
            # Stop if pointers meet or cross
            if self.front == node or self.front.next == node:
                node.next = None
                return False
            
            # Re-link
            temp = self.front.next
            self.front.next = node
            node.next = temp
            
            self.front = temp
            return True
        
        recurse(head)
