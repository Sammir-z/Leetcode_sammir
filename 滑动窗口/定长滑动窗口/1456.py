# https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel =0
        for i,c in enumerate(s):
            # 1、右端点进入窗口
            if c in 'aeiou':
                vowel += 1
            left = i-k+1
            if left < 0: # 窗口大小不足k，尚未形成第一个窗口， 这就是判断是否定长
                continue
            
            # 更新答案
            ans = max(ans, vowel)
            if ans == k: # 答案已经等于理论最大值，无需循环
                break
                
            # 左端点离开窗口，为下一个循环做准备
            if s[left] in 'aeiou':
                vowel -=1
        return ans 