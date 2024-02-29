class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        output = ListNode()
        curr = output

        while True:
            min_idx = None
            min_value = 99999999

            for idx, node in enumerate(lists):
                if node is not None and node.val < min_value:
                    min_idx = idx
                    min_value = node.val

            if min_idx is None:
                return output

            min_node = lists[min_idx]
            if lists[min_idx].next is None:
                lists.pop(min_idx)
            else:
                lists[min_idx] = lists[min_idx].next
            curr.next = min_node
            curr = curr.next


input_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
s = Solution()
result = s.mergeKLists(linked_lists)
while result:
    print(result.val, end=' ')
    result = result.next
print()
