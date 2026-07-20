class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        bucket_s = [0] * 26
        bucket_t = [0] * 26

        for i in range(len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')
            bucket_s[index_s] += 1
            bucket_t[index_t] += 1

        return bucket_s == bucket_t
