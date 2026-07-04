# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        beforeTarget = size - n - 1
        if size == 1 or beforeTarget < 0:
            return head.next
        curr = head
        while curr and beforeTarget > 0:
            curr = curr.next
            beforeTarget-=1
        curr.next = curr.next.next
        return head