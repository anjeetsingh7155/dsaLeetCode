class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        move = 0
        for i in range(len(nums)):
           if nums[i]!= 0:
            nums[move] , nums[i] =  nums[i] , nums[move]
            move+=1
        