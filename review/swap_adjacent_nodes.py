# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1, 2, 3, 4
        # 2, 1, 3, 4
        # 2, 1, 4, 3

        # 1, 2, 3, 4
        # 1, 2, 4, 3

        if not head or not head.next:
            return head

        newHead: ListNode = head.next
        head.next, newHead.next = self.swapPairs(head.next.next), head

        return newHead


s = Solution()
rst = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
while rst:
    print(rst.val, end=" ")
    rst = rst.next
print()
