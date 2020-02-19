#节点定义
class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        # 测试用例


class Solution():
    def reverseList1(self, head):
        p, q = head, head.next
        p.next = None

        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p

    def reserveList2(self, head):
        if not head.next:
            return head
        new_head = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)
    l1.next.next.next = LNode(99)
    s = Solution()
    l = s.reverseList1(l1)

    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)

    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)
    l1.next.next.next = LNode(99)
    l = s.reserveList2(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)

