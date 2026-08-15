class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        FirstSum = 0
        for i in range(k):
            FirstSum+=nums[i]
        maxSum = FirstSum
        for right in range(k,len(nums)):
            FirstSum+=nums[right]-nums[right-k]
            maxSum =max(maxSum,FirstSum)

        return maxSum/k

        