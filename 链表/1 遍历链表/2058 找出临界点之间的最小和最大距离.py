# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List, ListNode, int


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # 1、先遍历链表，转换成list
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        if n < 3:
            return [-1, -1]
        # 2、遍历list，找到所有的关键点
        critical_points = [] # 记录临界点的索引
        for i in range(1, n-1):
            if (nums[i] > nums[i-1] and nums[i] > nums[i+1]) or (nums[i]<nums[i-1] and nums[i]<nums[i+1]):
                critical_points.append(i)
        
        if len(critical_points) < 2:
            return [-1, -1]
        # 3、遍历关键点，找到最小距离和最大距离
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        for i in range(1, len(critical_points)):
            distance = critical_points[i] - critical_points[i-1]
            min_distance = min(min_distance, distance)
            # max_distance = max(max_distance, critical_points[i] - critical_points[0]
        return [min_distance, max_distance]