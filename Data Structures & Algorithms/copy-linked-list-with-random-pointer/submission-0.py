"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldMap={None:None}
        cur=head
        while cur:
            new=Node(cur.val)
            oldMap[cur]=new
            cur=cur.next

        cur=head
        while cur:
            copy=oldMap[cur]
            copy.next=oldMap[cur.next]
            copy.random=oldMap[cur.random]
            cur=cur.next
        return oldMap[head]