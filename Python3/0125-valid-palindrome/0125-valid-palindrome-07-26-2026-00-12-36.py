class Solution:
    def isPalindrome(self, s: str) -> bool:
        actualStr = ""
        if s == " ":
            return True
        for char in s:
            if char.isalnum():
                actualStr += char
                
        left =0 
        right = len(actualStr)-1
        lowerCaseActualStr = actualStr.lower()

        while left<right:
            if lowerCaseActualStr[left] == lowerCaseActualStr[right]:
                left+=1 
                right-=1
                continue
            else: return False
        return True
