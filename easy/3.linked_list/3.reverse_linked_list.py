from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:
        # First store the elements in a normal list: stack while scanning though the linked list
        current = head
        stack = []
        while current.val:
            stack.append(current.val)
            current = current.next
        reverse = ListNode(stack.pop())
        current = reverse
        # Build the reverse list by poping the element from the stack one after another
        while stack:
            current.next = ListNode(stack.pop())
            current = current.next
        return reverse

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        def reverse(head):
            if not head.next:
                return head
            else:
                reverse_next = reverse(head.next)
                return insert_end(reverse_next, head.val)

        def insert_end(head, n):
            current = head
            while current.next:
                current = current.next
            current.next = ListNode(n)
            return head
        return reverse(head)


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4, 5])
    print(head)
    print(Solution().reverseListRecursive(head))
