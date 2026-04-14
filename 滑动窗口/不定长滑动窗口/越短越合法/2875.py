# 2875. 无限数组的最短子数组
# 其实也就最多两次且长度超过target
class Solution:
    def minSizeSubarray(self, nums, target):
        n = len(nums)
        # 这里重塑nums
        # print(target, n)
        k = max(2,target//n+1)
        new_nums = []
        for _ in range(k):
            new_nums+=nums
        ans = n*k+1
        left = 0
        tmp_sum = 0 
        for rigth,x in enumerate(new_nums):
            # 1、进入滑动窗口
            tmp_sum+=x
            while tmp_sum>=target:
                # 2、更新
                if tmp_sum==target:
                    ans = min(ans, rigth - left + 1)
                    if ans == 1:
                        break
                # 3、出滑动窗口
                tmp_sum -= new_nums[left]
                left+=1
        return ans


s = Solution()
print(s.minSizeSubarray([1,2,3],5))