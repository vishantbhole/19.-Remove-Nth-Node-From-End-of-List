
#19. Remove Nth Node From End of List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # For printing the list nicely
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return "->".join(result)

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

# Helper function to build linked list from list
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
# Test case examples
def test():
    sol = Solution()

    head = build_linked_list([1, 2, 3, 4, 5])
    print("Original: ", head)
    result = sol.removeNthFromEnd(head, 2)
    print("After removing 2nd from end: ", result)

    head = build_linked_list([1])
    print("Original: ", head)
    result = sol.removeNthFromEnd(head, 1)
    print("After removing 1st from end: ", result)

    head = build_linked_list([1, 2])
    print("Original: ", head)
    result = sol.removeNthFromEnd(head, 1)
    print("After removing 1st from end: ", result)

if __name__ == "__main__":
    test()
