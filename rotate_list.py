
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


def print_node(node: ListNode):
    while node:
        print('val', node.val)
        node = node.next


def rotate(head: ListNode, k):
    count = 0
    values = []
    while head:
        values.append(head.val)
        head = head.next
        count += 1

    # print(values)
    nth_rotate = k % count
    node = ListNode()
    curr = node
    for i in range(count-nth_rotate, count):
        node.next = ListNode(values[i])
        node = node.next
    for i in range(0, count-nth_rotate):
        node.next = ListNode(values[i])
        node = node.next

    return curr.next


rotated = rotate(node, 2)
print_node(rotated)
# while rotated:
#     print(rotated.val)
#     rotated = rotated.next
