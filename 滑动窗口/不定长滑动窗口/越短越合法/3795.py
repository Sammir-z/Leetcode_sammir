# 3795. 不同元素和至少为 K 的最短子数组长度
from collections import Counter
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = n+1
        cnt = Counter()
        left = 0
        tmp = 0
        for right,x in enumerate(nums):
            # 1、入
            cnt[x] +=1
            if cnt[x] == 1:
                tmp +=x
            while tmp >= k:
                # 更新答案
                ans = min(ans, right - left + 1)

                # 3、出
                out = nums[left]
                cnt[out]-=1
                s-=out
                left+=1
        return ans if ans<n else -1