class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        k= len(nums)-1
       
        
        while k >=2: 
            right = k-1
            left = 0
            while left<right:
                if nums[right]+nums[left] >  nums[k]:
                     count+= right-left
                     right-=1
                else:
                    left+=1
            k-=1   
        return count

        
            
        