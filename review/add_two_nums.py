from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]
        num = str(int(num1) + int(num2))[::-1]

        node = ListNode()
        curr = node
        for dig in num:
            curr.next = ListNode(dig)
            curr = curr.next

        return node.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
s = Solution()
s.addTwoNumbers(l1, l2)
