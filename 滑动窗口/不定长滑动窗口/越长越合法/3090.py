# 3090. 每个字符最多出现两次的最长子字符串
from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, x in enumerate(s):
            cnt[x]+=1
            while cnt[x]>2:
                cnt[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans