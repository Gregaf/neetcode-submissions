class Solution:
    # Time: O(n^2) Space: O(1)
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                res = max(area, res)
        
        return res