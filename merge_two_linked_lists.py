
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNode(node1, node2):
    if node1 and node2:
        if node1.val <= node2.val:
            return node1, 1
        else:
            return node2, 2

    if node1 and not node2:
        return node1, 1

    if node2 and not node1:
        return node2, 2

    return None, None


def merge(node1, node2, output):
    node, elem = getNode(node1, node2)
    if not node:
        return

    output.next = ListNode(node.val)
    output = output.next

    if elem == 1:
        merge(node1.next, node2, output)
    else:
        merge(node1, node2.next, output)


node1 = ListNode(5)
node2 = ListNode(1, ListNode(2, ListNode(4)))
output = ListNode()
curr = output
merge(node1, node2, output)

while curr:
    print(curr.val)
    curr = curr.next
