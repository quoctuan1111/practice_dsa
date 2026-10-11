class Solution(object):
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0)
        dummy.next = head

        before = dummy
        curr = head
        group_size = 1

        while curr:
            node = curr
            count = 0

            while node and count < group_size:
                node = node.next
                count += 1

            if count % 2 == 0:
                group_tail = curr
                prev = node

                for _ in range(count):
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node

                before.next = prev
                before = group_tail

            else:
                for _ in range(count):
                    before = curr
                    curr = curr.next

            group_size += 1

        return dummy.next