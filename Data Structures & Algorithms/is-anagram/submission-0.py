class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCharMap = dict()
        for char in s:
            count = sCharMap.get(char, 0) + 1
            sCharMap[char] = count
        
        for char in t:
            currentCount = sCharMap.get(char, 0) - 1
            sCharMap[char] = currentCount
            if currentCount < 0:
                return False
        
        return True
