class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        front = 0
        answers = []

        for i in range(len(nums)):

            while len(dq) > front and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Remove outdated front
            if dq[front] <= i - k:
                front += 1

            if i >= k - 1:
                answers.append(nums[dq[front]])

        return answers