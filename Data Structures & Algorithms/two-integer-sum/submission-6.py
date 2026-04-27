class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        inverse_val_map = {num: i for i, num in enumerate(nums)}
        
        for i in range(len(nums)):
            target_value = target - nums[i]
            res = inverse_val_map.get(target_value)
            
            if res is not None and res != i:
                return [res, i] if i > res else [i, res]

        return [-1, -1] 
