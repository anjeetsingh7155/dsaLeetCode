class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)

        if k > len(s2):
            return False

        target = {}

        for char in s1:
            target[char] = target.get(char, 0) + 1

        window = {}

        # First window
        for i in range(k):
            char = s2[i]
            window[char] = window.get(char, 0) + 1

        # Check first window
        if window == target:
            return True

        # Sliding window
        for right in range(k, len(s2)):

            # Remove old/left character
            left_char = s2[right - k]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            # Add new/right character
            right_char = s2[right]
            window[right_char] = window.get(right_char, 0) + 1

            # Check current window
            if window == target:
                return True

        return False