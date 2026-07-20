class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [1,5,1,5] t = 10

        sum_map = {v:k for k,v in enumerate(nums)}
        for i in range(len(nums)):
            lookup = target - nums[i]
            val = sum_map.get(lookup)
            if val is not None and val != i:
                return [i, val]

        return [-1, -1]