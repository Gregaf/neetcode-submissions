class Solution:
    # Brute force O(n^2) time complexity, O(n) space for output array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)

        prefix_arr = [0] * len_nums
        suffix_arr = [0] * len_nums
        
        prefix_arr[0] = suffix_arr[len_nums - 1] = 1
        for i in range(1, len_nums):
                val_prev = prefix_arr[i - 1]
                val_curr = nums[i - 1]
                prefix_arr[i] = val_prev * val_curr

        for i in range(len_nums - 2, -1, -1):
                val_prev = suffix_arr[i + 1]
                val_curr = nums[i + 1]
                suffix_arr[i] = val_prev * val_curr

        product_arr = [0] * len_nums
        for i in range(len_nums):
                product_val = prefix_arr[i] * suffix_arr[i]
                product_arr[i] = product_val

        return product_arr 
