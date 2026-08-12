class Solution:
    def sortColors(self, nums: List[int]) -> None:
        write = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1

        back = len(nums) - 1
        i = write

        while i <= back:
            if nums[i] == 2:
                nums[back], nums[i] = nums[i], nums[back]
                back -= 1
            else:
                i += 1