class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        element = {}
        firstSum = 0
        best = 0

        for right in range(len(nums)):
            firstSum += nums[right]
            element[nums[right]] = element.get(nums[right], 0) + 1

            if right >= k:
                firstSum -= nums[right - k]

                element[nums[right - k]] -= 1

                if element[nums[right - k]] == 0:
                    del element[nums[right - k]]

            if right >= k - 1 and len(element) == k:
                best = max(best, firstSum)

        return best
        