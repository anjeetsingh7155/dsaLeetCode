class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        freq = dict()
        maxFreq = 0
        best =0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R],0)+1
            maxFreq = max(maxFreq, freq[s[R]])
            if (R-L+1)-maxFreq > k :
                freq[s[L]]-=1
                L+=1
            best = max(best,R-L+1)
        return best    