class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
  
        write =0
       
        for i,num in enumerate(nums):
            if num==val:
                continue
            nums[write] , nums[i] = nums[i] ,nums[write]
            write+=1

        return write