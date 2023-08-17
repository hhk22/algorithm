
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_list(linked_lists):
    output = ListNode()
    current = output

    if linked_lists is None or linked_lists == []:
        return []

    while True:
        min_value = float('inf')
        min_index = -1

        for idx, node in enumerate(linked_lists):
            if node and node.val < min_value:
                min_value = node.val
                min_index = idx

        output.next = linked_lists[min_index]
        output = output.next
        linked_lists[min_index] = linked_lists[min_index].next

        if not any(linked_lists):
            break

    return current.next


input_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [ListNode(1, ListNode(4, ListNode(5)))]
linked_lists = []
result = merge_k_sorted_list(linked_lists)
while result:
    print(result.val)
    result = result.next
