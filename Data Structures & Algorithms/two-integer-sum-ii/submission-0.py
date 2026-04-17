class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #
        num_len = len(numbers)

        l = 0
        r = len(numbers)

        # while [0 .. 5] l + r = target
        # [1, 2, 3, 4]
        #  3 - 1 = 2

        for i in range(num_len - 1):
            for j in range(i + 1, num_len):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return [-1, -1]
