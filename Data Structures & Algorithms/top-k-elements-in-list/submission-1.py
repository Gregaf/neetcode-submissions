class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()
        for num in nums:
            count = count_map.get(num, 0)
            count_map[num] = 1 + count
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in count_map.items():
            bucket = buckets[count]
            bucket.append(num)

        res = []

        i = len(buckets) - 1
        while k > 0 and i >= 0:
            bucket = buckets[i]
            bucket_len = len(bucket)
            
            i -= 1
            if bucket_len > 0:
                res += bucket
                k -= bucket_len
            
        return res