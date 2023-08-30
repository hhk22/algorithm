# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode):
    if not head or not head.next:
        return head

    newHead = head.next
    head.next, newHead.next = swapPairs(head.next.next), head
    return newHead


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
curr = swapPairs(node)
while curr:
    print(curr.val)
    curr = curr.next


