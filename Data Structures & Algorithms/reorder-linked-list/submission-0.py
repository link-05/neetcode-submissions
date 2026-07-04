# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None
        slow = head
        fast = head.next
        # Find middle
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
        # get node in reverse
        stack = []
        temp = slow.next
        slow.next = None
        slow = temp
        while slow:
            stack.append(slow)
            slow = slow.next
        slow = head
        while stack:
            temp = slow.next
            target = stack.pop()
            slow.next = target
            target.next = temp
            slow = temp
        
        return None

