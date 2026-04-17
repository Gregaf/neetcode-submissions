class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Sorted approach, O(logn + logm) time complexity (depends on sort)
        # sort_s = sorted(s)
        # sort_t = sorted(t)

        # for i in range(len(sort_s)):
        #     if sort_s[i] != sort_t[i]:
        #         return False

        count_map_s, count_map_t = dict(), dict()

        for i in range(len(s)):
            count_map_s[s[i]] = 1 + count_map_s.get(s[i], 0)
            count_map_t[t[i]] = 1 + count_map_t.get(t[i], 0)
        
        return count_map_s == count_map_t