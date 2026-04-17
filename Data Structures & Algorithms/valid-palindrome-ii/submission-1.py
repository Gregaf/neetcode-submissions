class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                sL = self.isPalindrome(s[l + 1:r + 1])
                sR = self.isPalindrome(s[l:r])
                hasPalindrome = sL or sR

                if not hasPalindrome:
                    return False

            l += 1
            r -= 1
        
        return True
