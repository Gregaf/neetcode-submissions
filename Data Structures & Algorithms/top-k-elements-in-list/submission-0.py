class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()

        for num in nums:
            curr = count_map.get(num, 0)
            count_map[num] = curr + 1
        
        pairs = list(count_map.items())
        pairs.sort(key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            key, val = pairs[i]
            res.append(key)

        return res