from typing import List


# 闭区间

def lower_bound(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left, right = 0, n-1  # 闭区间[left, right]

    while left<= right:
        mid = (left + right) // 2 # (left + (right - left)//2)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return left

# 左边闭右开区间
def lower_bound2(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left, right = 0, n  # 左边闭右开区间[left, right)

    while left < right:
        mid = (left + right) // 2 # (left + (right - left)//2)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid 
    return left
 # 左右开区间
def lower_bound3(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left, right = 0, n  # 左右开区间（left, right）

    while left+1 < right:
        mid = (left + right) // 2 # (left + (right - left)//2)
        if nums[mid] < target:
            left = mid
        else:
            right = mid 
    return right