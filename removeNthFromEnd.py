


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        curr = dummy
        end = head
        while n > 0 and end:
            end = end.next
            n -= 1
        while end:
            curr = curr.next
            end = end.next
        curr.next = curr.next.next
        return dummy.next
