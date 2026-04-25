class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        largest_seq = 0
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            
            j = nums[i] + 1
            while j in nums_set:
                j += 1
            largest_seq = max(largest_seq, j - nums[i])
        
        return largest_seq
    