class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_floor = len(nums) // 2
        # count_map = dict()

        # for num in nums:
        #     curr_count = count_map.get(num, 0)
        #     count_map[num] = curr_count + 1
        
        # for key, val in count_map.items():
        #     if val > majority_floor:
        #         return key

        sorted_nums = sorted(nums)
        return sorted_nums[majority_floor]