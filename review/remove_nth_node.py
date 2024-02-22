from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) == 1:
            return None

        target_idx = len(nodes) - n
        nodes = nodes[:target_idx] + nodes[target_idx+1:]

        curr = ListNode()
        output = curr
        for node in nodes:
            curr.next = ListNode(node.val)
            curr = curr.next

        return output.next


def get_tree(node: ListNode):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


s = Solution()
rst = s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
assert get_tree(rst) == [1, 2, 3, 5]
rst = s.removeNthFromEnd(ListNode(1), 1)
assert get_tree(rst) == []
rst = s.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
assert get_tree(rst) == [2]
