# 209. 长度最小的子数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        s, left=0, 0
        for right, x in enumerate(nums): # x : nums[right]
            s +=x
            # # while 循环结束后更新
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left+=1
            # if s >= target:
            #     ans = min(ans, right - left + 1)
            while s >= target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left +=1
        return ans if ans<=n else 0