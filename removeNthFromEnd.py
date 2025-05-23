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
