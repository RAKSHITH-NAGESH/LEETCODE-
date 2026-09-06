class Solution:
    def numDistinct(self, s, t):
        dp = [1] + [0] * len(t)

        for c in s:
            for j in range(len(t), 0, -1):
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[len(t)]