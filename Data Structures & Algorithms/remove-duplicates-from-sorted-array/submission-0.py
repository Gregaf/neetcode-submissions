class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = f = 0
        len_nums = len(nums)

        while f < len_nums:
            while f < len_nums and nums[f] == nums[s]:
                f += 1
            s += 1

            if f < len_nums:
                nums[s] = nums[f]

        return s
