class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for i in range(len(strs)):
            sig = ''.join(sorted(strs[i]))
            if sig in groups:
                groups[sig].append(strs[i])
            else : groups[sig] = [strs[i]]
        return list(groups.values())
