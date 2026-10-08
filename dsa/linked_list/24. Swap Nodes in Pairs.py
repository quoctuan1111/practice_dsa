# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        new_head = head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            nextNode = head.next.next

            head.next.next = head
            head.next = nextNode
            prev = head
            head = nextNode
        return new_head