class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            curr = nums[m]

            if curr == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1