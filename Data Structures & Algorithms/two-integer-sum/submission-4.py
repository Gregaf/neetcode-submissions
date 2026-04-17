class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] = nums[j]

        # Brute force approach
        nums_len = len(nums)

        diff_map = dict()
        for i in range(nums_len):
            diff = target - nums[i]
            index = diff_map.get(diff)
            
            if index is not None:
                return [index, i]
            
            diff_map[nums[i]] = i

        # for i in range(nums_len):
        #     for j in range(i+1, nums_len):
        #         if target - nums[i] == nums[j]:
        #             return [i, j]
        
        return [0, 0]