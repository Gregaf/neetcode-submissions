class Solution:
    # Brute force O(n^2) time complexity, O(n) space for output array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
    
        product_arr = []
        for i in range(len_nums):
            product_curr = 1
            for j in range(len_nums):
                if i == j:
                    continue
            
                product_curr *= nums[j]
            product_arr.append(product_curr)

        return product_arr    
