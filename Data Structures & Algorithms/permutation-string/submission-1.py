def getSlot(char: str) -> int:
    return ord(char) - ord("a")

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_map_s1 = [0] * 26
        for c in s1:
            count_map_s1[getSlot(c)] += 1

        count_map_s2 = [0] * 26
        for i in range(len(s1)):
            count_map_s2[getSlot(s2[i])] += 1
        
        l=0
        r=len(s1) - 1
        while r < len(s2):
            if count_map_s1 == count_map_s2:
                return True
            
            count_map_s2[getSlot(s2[l])] -= 1
            l += 1
            r += 1
            if r < len(s2):
                count_map_s2[getSlot(s2[r])] += 1            

        return False