
# Sort a linked list in O(n log n) time using constant space complexity.


def print_list(node):
    while node and node.next:
        print(str(node.val) + ' -> ', end='')
        node = node.next
    print(str(node.val))


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        def merge(left, right):
            dummy = ListNode(0)
            current = dummy

            while left and right:
                if left.val <= right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next

            if not left:
                current.next = right
            if not right:
                current.next = left

            return dummy.next

        if not head or not head.next:
            return head

        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        right_node = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(right_node)
        return merge(left, right)


# Test Cases
s = Solution()

head1 = ListNode(4)
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(3)
print_list(head1)
node = s.sortList(head1)
print_list(node)


head2 = ListNode(-1)
head2.next = ListNode(5)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(0)
head2.next.next.next.next.next = ListNode(-2)
head2.next.next.next.next.next.next = ListNode(-15)
print_list(head2)
node = s.sortList(head2)
print_list(node)
