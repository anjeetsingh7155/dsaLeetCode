class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = dict()
        window = dict()

        left = 0
        have = 0

        bestWindow = None
        bestLength = float("inf")

        # Build frequency map for t
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        # Number of distinct characters required
        required = len(need)

        # Expand window using Right
        for Right in range(len(s)):

            char = s[Right]

            # Add character to window
            window[char] = window.get(char, 0) + 1

            # Check if requirement for this character is satisfied
            if char in need and window[char] == need[char]:
                have += 1

            # Window is valid
            while have == required:

                # Current window length
                width = Right - left + 1

                # Save smallest window
                if width < bestLength:
                    bestLength = width
                    bestWindow = (left, Right)

                # Remove left character
                leftChar = s[left]
                window[leftChar] -= 1

                # Requirement is no longer satisfied
                if leftChar in need and window[leftChar] < need[leftChar]:
                    have -= 1

                # Move left pointer
                left += 1

        # No valid window found
        if bestWindow is None:
            return ""

        # Return best substring
        return s[bestWindow[0]:bestWindow[1] + 1]