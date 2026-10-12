class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        counts = [0] * 32

        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    counts[bit] += 1

        result = 0

        for _ in range(k):
            num = 0

            for bit in range(32):
                if counts[bit] > 0:
                    num |= 1 << bit
                    counts[bit] -= 1

            result = (result + num * num) % MOD

        return result