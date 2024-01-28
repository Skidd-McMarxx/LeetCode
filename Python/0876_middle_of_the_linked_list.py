# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        mid_node = head
        while head and head.next:
            mid_node = mid_node.next
            head = head.next.next
        return mid_node