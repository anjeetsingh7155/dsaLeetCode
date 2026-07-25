class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        if len(numbers)==0:return []

        while left<right :
            sum = numbers[right]+numbers[left]
            if sum ==target :
                return [left + 1, right + 1]
            elif sum<target : left+=1
            else: right-=1
        