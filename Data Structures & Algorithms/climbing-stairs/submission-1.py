class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None] * n
        print(cache)

        def climb(cache, n):
            if n < 0:
                return 0
            
            c_index = n - 1

            if cache[c_index] is not None:
                return cache[c_index]

            one_step = climb(cache, n - 1)
            two_step = climb(cache, n - 2)

            val = 1 if n == 0 else 0
            
            res = val + one_step + two_step
            cache[c_index] = res

            return res

        return climb(cache, n)