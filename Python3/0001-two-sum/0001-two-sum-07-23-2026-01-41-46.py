class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums):
                if(v1+v2 == target):
                    if(i1 == i2):
                        continue
                    numResult = [i1,i2]
                    return numResult
        