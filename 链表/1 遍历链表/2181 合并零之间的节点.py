# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode, int
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1、 先遍历链表，转成list
        nums = []
        while head: 
            nums.append(head.val)
            head = head.next
        ans = []
        # 2遍历list，找到所有的值
        tmp_sum = 0
        for num in nums:
            # 说明遇到了一个0，并且之前的和不为0了，说明之前的和是一个新的节点的值了
            if num == 0 and tmp_sum != 0: 
                ans.append(tmp_sum)
                tmp_sum = 0
            else:
                tmp_sum += num
        # 3、把ans转成链表
        dummy = ListNode(-1)
        current = dummy
        for val in ans:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

