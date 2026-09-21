class Solution:
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            value = num % k

            new_dp = [0] * k

            # Start a new subarray with this number
            new_dp[value] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * value) % k
                    new_dp[new_remainder] += dp[r]

            dp = new_dp

            # Add all subarrays ending here
            for r in range(k):
                result[r] += dp[r]

        return result