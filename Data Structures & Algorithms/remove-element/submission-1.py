class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        l = 0
        r = len(nums) - 1

        while l <= r:
            while l <= r and nums[l] != val:
                l += 1
            while l <= r and nums[r] == val:
                r -= 1
            
            if l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
        
        return l
