class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        element_bucket_map = dict()

        for num in nums:
            count = element_bucket_map.get(num, 0)

            count += 1
            element_bucket_map[num] = count
        
        buckets = [[] for n in range(len(nums))]

        for key, val in element_bucket_map.items():
            buckets[val - 1].append(key)
        
        res = []
        i = len(nums) - 1
        while (k != 0):
            current = buckets[i]
            k -= len(current)
            res += current
            i -= 1

        return res