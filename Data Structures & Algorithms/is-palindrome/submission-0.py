class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(1) Space, O(N) Time complexity
        alnum_s = "".join([x.lower() for x in s if x.isalnum()])

        l = 0
        r = len(alnum_s) - 1

        while l < r:
            if alnum_s[l] != alnum_s[r]:
                
                return False

            l += 1
            r -= 1

        return True