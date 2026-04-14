# 3. 无重复字符的最长子串
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter() # hashmap, key:char, value: int， 不用dict是因为dict的value不方便 加等于1
        left = 0
        for right, x in enumerate(s):
            cnt[x]+=1
            while cnt[x]>1:
                cnt[s[left]]-=1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        