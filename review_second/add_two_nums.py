from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()

        l1_val = ""
        while l1:
            l1_val += str(l1.val)
            l1 = l1.next

        l2_val = ""
        while l2:
            l2_val += str(l2.val)
            l2 = l2.next

        tot_val = int(l1_val[::-1]) + int(l2_val[::-1])
        tot_val = str(tot_val)[::-1]

        tmp_node = new_node
        for val in tot_val:
            tmp_node.next = ListNode(int(val))
            tmp_node = tmp_node.next

        return new_node.next


def print_nodes(node: ListNode):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


s = Solution()
rst = s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
print_nodes(rst)
rst = s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(9))), ListNode(5, ListNode(6, ListNode(4, ListNode(9)))))
print_nodes(rst)
