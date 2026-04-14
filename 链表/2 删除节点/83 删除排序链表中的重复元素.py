class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4)))))))
    print(Solution().deleteDuplicates(head))