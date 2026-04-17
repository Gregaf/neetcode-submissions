class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] = nums[j]
        
        numsInvertedMap = dict()
        
        # { num: index }
        for i in range(len(nums)):
            numsInvertedMap[nums[i]] = i
        
        for i in range(len(nums)):
            sumKey = target - nums[i]
            
            sumIndex = numsInvertedMap.get(sumKey)

            if sumIndex != None and sumIndex != i:
                return [i, sumIndex]
        
        return [-1, -1]