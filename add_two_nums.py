from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(3n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pos = 1
        l1_val = 0
        while l1:
            l1_val += l1.val * pos
            pos *= 10
            l1 = l1.next

        pos = 1
        l2_val = 0
        while l2:
            l2_val += l2.val * pos
            pos *= 10
            l2 = l2.next

        node = ListNode()
        outputNode = node
        for i in str(l1_val+l2_val)[::-1]:
            outputNode.next = ListNode(val=i)
            outputNode = outputNode.next

        return node.next


class Solution02:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1
        carry = 0

        while l1 and l2:
            prev = l1
            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
            l1, l2 = l1.next, l2.next

        tail = l1 or l2
        prev.next = tail

        while tail:
            carry, tail.val = divmod(tail.val + carry, 10)
            prev, tail = tail, tail.next

        if carry:
            prev.next = ListNode(val=1)

        return res


def list_to_node(values):
    node = ListNode(values.pop(0))
    res = node
    while values:
        node.next = ListNode(values.pop(0))
        node = node.next

    return res


def node_to_list(node: ListNode):
    while node:
        print(node.val, end='')
        node = node.next


t1 = [9, 9, 9, 9, 9, 9, 9]
# t1 = [9, 9, 9, 9]
t2 = [9, 9, 9, 9]

t1_node = list_to_node(t1)
t2_node = list_to_node(t2)

s = Solution02()
tt = s.addTwoNumbers(t1_node, t2_node)
node_to_list(tt)
