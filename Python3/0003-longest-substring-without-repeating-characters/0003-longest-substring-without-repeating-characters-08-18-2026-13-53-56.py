class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        last = dict()
        maxLength =0

        for right in range(0,len(s)):
            if s[right] in last.keys() and last[s[right]]>=left :
                left = last[s[right]]+1
                last[s[right]] = right
            else:
                last[s[right]] = right
                maxLength = max(maxLength , right-left+1)

        return  maxLength
        