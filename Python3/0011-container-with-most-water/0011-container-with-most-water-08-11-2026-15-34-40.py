class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ResultMax = 0
        while left<right:
            if(height[left]<height[right]):
                n = right - left
                area = n * height[left]
                if area>ResultMax :
                    ResultMax = area 
                left+=1
            else:
                n = right - left
                area = n * height[right]
                if area>ResultMax :
                    ResultMax = area 
                right-=1

        return ResultMax