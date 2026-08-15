class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 :
            return 0
        AnsSet = set(nums)
        best = 1
        for i in AnsSet:
            if i-1 in AnsSet:
                continue
            length= 1
            while i+length in AnsSet:
                length+=1
            best = max(best,length) 
        return best

