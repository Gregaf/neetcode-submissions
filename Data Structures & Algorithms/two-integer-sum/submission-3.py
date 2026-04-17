class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] = nums[j]
        
        # Brute force approach
        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if target - nums[i] == nums[j]:
                    return [i, j]
        
        return [0, 0]