# Definition for singly-linked list.

from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1、先遍历链表，转换成list
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        # 2、计算每个部分的长度
        n = len(nums)
        part_length = n // k
        ex_length = n % k # 余数部分，前ex_length个部分需要多一个节点
        ans = []
        index = 0
        for i in range(k):
            current_part_length = part_length + (1 if i < ex_length else 0) # 当前部分的长度
            if current_part_length == 0:
                ans.append(None)
            else:
                # 重组链表
                dummy = ListNode(-1)
                current = dummy
                for j in range(current_part_length):
                    current.next = ListNode(nums[index])
                    current = current.next
                    index += 1
                ans.append(dummy.next)
        return ans