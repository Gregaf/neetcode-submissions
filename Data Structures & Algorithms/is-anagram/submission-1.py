class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # FIRST PASS: Not as easily readable, but same time complexity and memory        
        # sCharMap = dict()
        # for char in s:
        #     count = sCharMap.get(char, 0) + 1
        #     sCharMap[char] = count
        
        # for char in t:
        #     currentCount = sCharMap.get(char, 0) - 1
        #     sCharMap[char] = currentCount
        #     if currentCount < 0:
        #         return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            countS[charS] = 1 + countS.get(charS, 0)
            countT[charT] = 1 + countT.get(charT, 0)

        return countS == countT
