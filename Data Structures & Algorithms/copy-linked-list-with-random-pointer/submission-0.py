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
        n_dict = {}
        has_random = []
        if not head:
            return None
        dummy = Node(0)
        deepCopy = dummy
        curr = head
        while curr:
            if curr.random:
                has_random.append(curr)
            # make a deep copy
            copy = Node(curr.val)
            n_dict[curr] = copy
            deepCopy.next = copy
            deepCopy = copy
            curr = curr.next
        while has_random:
            target = has_random.pop()
            target_copy = n_dict[target]
            target_random_copy = n_dict[target.random]
            target_copy.random = target_random_copy
        
        return dummy.next
