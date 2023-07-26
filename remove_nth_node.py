from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    nodes = []
    while head:
        nodes.append(head)
        head = head.next

    if len(nodes) == 1:
        return curr.next

    idx = len(nodes) - n
    if idx == 0:
        curr = nodes[idx+1]
    else:
        nodes[idx-1].next = nodes[idx].next
    return curr


def show(head):
    while head:
        print(head.val)
        head = head.next


# node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node = ListNode(1, ListNode(2))
show(removeNthFromEnd(node, 2))

