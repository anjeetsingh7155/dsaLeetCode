class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        total = sum(cardPoints)

        # Number of cards we leave in the middle
        w = n - k

        # Sum of first window
        windowSum = sum(cardPoints[:w])
        minSum = windowSum

        # Sliding window
        for r in range(w, n):
            windowSum += cardPoints[r] - cardPoints[r - w]
            minSum = min(minSum, windowSum)

        # Maximum points = total - minimum middle window
        return total - minSum

