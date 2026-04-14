# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_s = set(nums)
        cur = dummy = ListNode(next = head)
        while cur.next:
            if cur.next.val in num_s:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
