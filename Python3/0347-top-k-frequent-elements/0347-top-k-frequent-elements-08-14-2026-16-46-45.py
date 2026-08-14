class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= dict()
        result = list()
        for v in nums:
            count[v] = count.get(v,0)+1
        bucket = [[] for i in range(len(nums)+1)]
        for num , frequency in count.items():
            bucket[frequency].append(num)
            
        for i in range(len(nums),0,-1):
            for nums in bucket[i]:
                result.append(nums)
                if len(result)==k:
                    return result
            
