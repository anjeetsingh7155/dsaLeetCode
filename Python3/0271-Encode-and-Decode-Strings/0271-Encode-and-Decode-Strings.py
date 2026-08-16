class Solution:
    def encode(self, arr):
        res = ""

        for s in arr:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        ptr = 0

        while ptr < len(s):
            j = s.index("#", ptr)

            length = int(s[ptr:j])

            res.append(s[j + 1:j + 1 + length])

            ptr = j + 1 + length

        return res