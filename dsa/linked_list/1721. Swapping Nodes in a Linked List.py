# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        slow = head
        for _ in range(k - 1):
            curr = curr.next
        first = curr
        while curr and curr.next:
            slow = slow.next
            curr = curr.next
        first.val, slow.val = slow.val, first.val
        return head
